"""
Address book module.
"""

from collections import UserDict
from datetime import datetime
from contacts.record import Record


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
            raise ValueError(f"Contact {new_record.name.value} already exists")
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
        raise ValueError(f"Contact {contact_name} not found")

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
            raise ValueError(f"Contact {contact_name} not found")
        del self.data[normalized_name]

    def upcoming_birthdays(self, days: int) -> dict:
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
            date.strftime("%d.%m.%Y"): name
            for date, name in sorted(upcoming_birthdays.items())
        }
        return "\n".join(f"{date}: {name}" for date, name in sorted_birthdays.items())
