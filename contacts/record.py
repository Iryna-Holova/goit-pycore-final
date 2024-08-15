"""
Record module.
"""

from typing import List
from contacts.name import Name
from contacts.birthday import Birthday
from contacts.phone import Phone
from contacts.email import Email


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
        self.emails: List[Email] = []

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

    def add_email(self, email: str) -> None:
        """
        Adds a new email address to the record.

        Args:
            email (str): The email address to add.

        Returns:
            None

        Raises:
            ValueError: If the email address already exists in the record.
        """
        new_email = Email(email)
        if new_email in self.emails:
            raise ValueError(f"❌ Email {email} already exists")
        self.emails.append(new_email)

    def remove_email(self, email: str) -> None:
        """
        Removes an email address from the list of emails in the `Record` instance.

        Args:
            email (str): The email address to remove.

        Raises:
            ValueError: If the email address is not found in the list of emails.

        Returns:
            None
        """
        email_to_remove = Email(email)
        if email_to_remove in self.emails:
            self.emails.remove(email_to_remove)
        else:
            raise ValueError(f"❌ Email address {email} not found")

    def edit_email(self, old_email: str, new_email: str) -> None:
        """
        Edits an email address in the record.

        Args:
            old_email (str): The email address to be replaced.
            new_email (str): The new email address.

        Returns:
            None

        Raises:
            ValueError: If the old email address is not found or the new email
            address already exists.
        """
        old_field = Email(old_email)
        try:
            email_index = next(
                i for i, email in enumerate(self.emails) if email == old_field
            )
        except StopIteration as exc:
            raise ValueError(f"❌ Email address {old_email} not found") from exc
        new_field = Email(new_email)
        if new_field in self.emails:
            raise ValueError(f"❌ Email {new_email} already exists")
        self.emails[email_index] = new_field

    def find_email(self, email: str) -> Email:
        """
        Finds an email address in the record.

        Args:
            email (str): The email address to find.

        Returns:
            Email: The found email address.

        Raises:
            ValueError: If the email address is not found.
        """
        if Email(email) in self.emails:
            return Email(email)
        raise ValueError(f"❌ Email address {email} not found")

    def __str__(self):
        phones_str = "; ".join(str(phone) for phone in self.phones)
        emails_str = "; ".join(str(email) for email in self.emails)
        return f"📞 name: {self.name.value:10} phones: {phones_str} emails: {emails_str}"
