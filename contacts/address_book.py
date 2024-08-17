"""
Address book module.
"""

from collections import UserDict
from datetime import datetime
from fuzzywuzzy import process
from tabulate import tabulate
from helpers.colors import warning, red
from contacts.record import Record
from constants.validation import DATE_FORMAT, validation_errors
from constants.info_messages import info_messages


class AddressBook(UserDict):
    """
    Address book class which holds records.
    """

    def add_record(self, new_record: Record) -> None:
        """
        Adds a new record to the address book.

        Args:
            new_record (Record): The record to be added.

        Raises:
            ValueError: If a contact with the same name already exists.
        """
        normalized_name = new_record.name.value.lower()
        if normalized_name in self.data:
            raise ValueError(
                validation_errors["duplicate_name"].format(new_record.name.value)
            )
        self.data[normalized_name] = new_record

    def find(self, contact_name: str) -> Record:
        """
        Finds a record in the address book.

        Args:
            contact_name (str): The name of the contact.

        Raises:
            ValueError: If the contact is not found.

        Returns:
            Record: The record with the given name.
        """
        normalized_name = contact_name.strip().lower()
        if normalized_name in self.data:
            return self.data[normalized_name]
        raise ValueError(validation_errors["name_not_found"].format(contact_name))

    def delete(self, contact_name: str) -> None:
        """
        Deletes a record from the address book.

        Args:
            contact_name (str): The name of the contact.

        Raises:
            ValueError: If the contact is not found.
        """
        normalized_name = contact_name.lower()
        if normalized_name not in self.data:
            raise ValueError(validation_errors["name_not_found"].format(contact_name))
        del self.data[normalized_name]

    def upcoming_birthdays(self, days: int, short: bool = False) -> str:
        """
        Calculate upcoming birthdays within a number of days for a given list
        of users.

        Args:
            book (AddressBook): An instance of the `AddressBook` class.
            days (int): The number of days to check for upcoming birthdays.

        Returns:
            dict: A dictionary with "congratulation_date" keys and
            corresponding "name" values for upcoming birthdays within the
            given number of days.
        """
        today = datetime.today().date()
        upcoming_birthdays = {}

        for contact in self.data.values():
            if contact.birthday is None:
                continue
            birthday = contact.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            if (birthday_this_year - today).days < days:
                upcoming_birthdays[birthday_this_year] = contact.name.value

        sorted_birthdays = {
            date.strftime(DATE_FORMAT): name
            for date, name in sorted(upcoming_birthdays.items())
        }
        if not sorted_birthdays:
            return warning(f"No birthdays in the next {days} days.")

        headers = ["Date", "Name"]
        colored_headers = [red(header) for header in headers]
        table = [[date, name] for date, name in sorted_birthdays.items()]

        return tabulate(table, headers=colored_headers, tablefmt="grid")

    def search(self, search_term: str) -> list:
        """
        Searches for contacts by name or phone number.
        Args:
            search_term (str): The term to search for in the contact names and
            phone numbers.
        Returns:
            list: A list of `Record` instances that match the search term.
        """
        search_term = search_term.lower()
        results = []

        for record in self.data.values():
            if search_term in record.name.value.lower():
                results.append(record)
                continue

            for phone in record.phones:
                if search_term in str(phone):
                    results.append(record)
                    break

        return results

    def smart_search(self, search_term: str, limit: int = 5) -> list:
        """
        Smart search that finds contacts even with typos and suggests contacts
          as the user types.
        Args:
            search_term (str): The term to search for in the contact names and
              phone numbers.
            limit (int): The maximum number of suggestions to return.
            Returns:
            list: A list of `Record` instances that match the search term with
              fuzzy matching.
        """
        search_term = search_term.lower()
        names = [record.name.value for record in self.data.values()]
        phone_numbers = [
            (str(phone), record.name.value)
            for record in self.data.values()
            for phone in record.phones
        ]

        # Get fuzzy matches for names
        name_matches = process.extract(search_term, names, limit=limit)
        matched_names = [
            match[0] for match in name_matches if match[1] >= 70
        ]  # 70% similarity threshold

        # Get matches for phone numbers
        phone_matches = [name for phone, name in phone_numbers if search_term in phone]

        # Combine name and phone matches
        matched_names.extend(phone_matches)
        matched_names = list(set(matched_names))  # Remove duplicates

        results = []
        for name in matched_names:
            record = self.data.get(name.lower())  # Fetch the Record object
            if record:  # Ensure that it's a valid Record object
                results.append(record)

        # Return just the list of Record objects
        return results
