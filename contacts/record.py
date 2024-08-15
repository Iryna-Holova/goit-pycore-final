"""
Record module.
"""

from typing import List
from contacts.name import Name
from contacts.phone import Phone
from contacts.birthday import Birthday
from contacts.address import Address


class Record:
    """
    Class representing a contact in the address book.

    Attributes:
        name (Name): The name of the contact.
        phones (List[Phone]): The list of phone numbers in the contact.
        birthday (Birthday | None): The birthday of the contact.
        address (Address | None): The address of the contact.
    """

    def __init__(self, contact_name: str) -> None:
        """
        Initializes a new Record instance.

        Args:
            contact_name (str): The name of the contact.

        Returns:
            None
        """
        self.name = Name(contact_name)
        self.phones: List[Phone] = []
        self.birthday: Birthday | None = None
        self.address: Address | None = None

    def add_phone(self, phone: str) -> None:
        """
        Adds a new phone number to the record.

        Args:
            phone (str): The phone number to add.

        Returns:
            None

        Raises:
            ValueError: If the phone number already exists in the record.
        """
        new_phone = Phone(phone)
        if new_phone in self.phones:
            raise ValueError(f"Phone number {phone} already exists")
        self.phones.append(new_phone)

    def remove_phone(self, phone: str) -> None:
        """
        Removes a phone number from the list of phones in the `Record`
        instance.

        Args:
            phone (str): The phone number to remove.

        Raises:
            ValueError: If the phone number is not found in the list of phones.

        Returns:
            None
        """
        phone_to_remove = Phone(phone)
        if phone_to_remove in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone number {phone} not found")

    def add_birthday(self, birthday: str) -> None:
        """
        Adds a birthday to the record.

        Args:
            birthday (str): The birthday to be added in the format DD.MM.YYYY.

        Returns:
            None
        """
        self.birthday = Birthday(birthday)

    def add_address(self, address: str) -> None:
        """
        Adds an address to the record.

        Args:
            address (str): The address to be added.

        Returns:
            None
        """
        self.address = Address(address)

    def __str__(self):
        phones_str = ", ".join(map(str, self.phones)) if self.phones else "N/A"
        return (
            f"name: {self.name}\n"
            f"phones: {phones_str}\n"
            f"birthday: {self.birthday if self.birthday else 'N/A'}\n"
            f"address: {self.address if self.address else 'N/A'}\n"
        )
