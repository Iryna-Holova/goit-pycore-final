"""
Address book module.
"""

from collections import UserDict
from datetime import datetime, timedelta
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
        normalized_name = contact_name.lower()
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

    def get_upcoming_birthdays(self) -> list:
        """
        Calculate upcoming birthdays within a week for a given list of users.

        Args:
            users (list): A list of dictionaries containing user information
            with keys "name" and "birthday".

        Returns:
            list: A list of dictionaries with "name" and "congratulation_date"
            keys for upcoming birthdays within a week.
        """
        today = datetime.today().date()
        upcoming_birthdays = []

        for contact in self.data.values():
            if contact.birthday is None:
                continue
            birthday = contact.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            if (birthday_this_year - today).days < 7:
                if birthday_this_year.weekday() >= 5:
                    congrats_date = birthday_this_year + timedelta(
                        days=(7 - birthday_this_year.weekday())
                    )
                else:
                    congrats_date = birthday_this_year

                upcoming_birthdays.append(
                    {
                        "name": contact.name.value,
                        "congratulation_date": congrats_date.strftime("%Y.%m.%d"),
                    }
                )

        return upcoming_birthdays
