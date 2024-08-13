"""
Record module.
"""

from typing import List
from contacts.name import Name
from contacts.birthday import Birthday
from contacts.phone import Phone


class Record:
    """
    Class representing a record.

    Attributes:
        name (Name): The name of the record.
        phones (List[Phone]): The list of phone numbers in the record.
        birthday (Birthday | None): The birthday of the record.
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
            raise ValueError(f"❌ Phone {phone} already exists")
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
            raise ValueError(f"❌ Phone number {phone} not found")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Edits a phone number in the record.

        Args:
            old_phone (str): The phone number to be replaced.
            new_phone (str): The new phone number.

        Returns:
            None

        Raises:
            ValueError: If the old phone number is not found or the new phone
            number already exists.
        """
        old_field = Phone(old_phone)
        try:
            phone_index = next(
                i for i, phone in enumerate(self.phones) if phone == old_field
            )
        except StopIteration as exc:
            raise ValueError(f"❌ Phone number {old_phone} not found") from exc
        new_field = Phone(new_phone)
        if new_field in self.phones:
            raise ValueError(f"❌ Phone {new_phone} already exists")
        self.phones[phone_index] = new_field

    def find_phone(self, phone: str) -> Phone:
        """
        Finds a phone number in the record.

        Args:
            phone (str): The phone number to find.

        Returns:
            Phone: The found phone number.

        Raises:
            None
        """
        if Phone(phone) in self.phones:
            return Phone(phone)
        raise ValueError(f"❌ Phone number {phone} not found")

    def add_birthday(self, birthday: str) -> None:
        """
        Adds a birthday to the record.

        Args:
            birthday (str): The birthday to be added in the format DD.MM.YYYY.

        Returns:
            None
        """
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"📞 name: {self.name.value:10} phones: {'; '.join(str(phone) for phone in self.phones)}"
