"""
Controllers module.

The controllers module contains functions that interact with the user and
modify the address book.
"""

from decorators.input_error import input_error
from contacts.address_book import AddressBook
from contacts.record import Record


@input_error
def add_contact(book: AddressBook) -> str:
    """
    Adds a new contact to the `book` if the name is not already in the
    `book` or adds the phone number to an existing contact.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A message indicating whether the contact was added or updated, or
        if the input is invalid.
    """
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    try:
        record = book.find(name)
        record.add_phone(phone)
        return "✅ Contact updated."
    except ValueError:
        new_record = Record(name)
        new_record.add_phone(phone)
        book.add_record(new_record)
        return "✅ Contact added."


@input_error
def change_contact(book: AddressBook) -> str:
    """
    Changes an existing contact's phone number in the address book.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A message indicating whether the contact was updated or if the
        input is invalid.
    """
    name = input("Enter name: ")
    old_phone = input("Enter old phone number: ")
    new_phone = input("Enter new phone number: ")

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "✅ Contact updated."


@input_error
def get_phones(book: AddressBook) -> str:
    """
    Returns a string containing the phone numbers of the contact with the
    given name in the `book`.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the phone numbers of the contact with the
        given name.
    """
    name = input("Enter name: ")

    record = book.find(name)
    return "\n".join([str(phone) for phone in record.phones])


def get_contacts(book: AddressBook) -> str:
    """
    Returns a string containing the names and phone numbers of all contacts
    in the `book`.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the names and phone numbers of all contacts
        in the `book`.
    """
    if not book.data:
        return "❗ There are no contacts."

    contacts = book.data
    return "\n".join([str(contact) for contact in contacts.values()])


@input_error
def add_birthday(book: AddressBook) -> str:
    """
    Adds a birthday to the contact with the given name in the `book`.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A message indicating whether the birthday was added or if the
        input is invalid.
    """
    name = input("Enter name: ")
    birthday = input("Enter birthday: ")

    record = book.find(name)
    record.add_birthday(birthday)
    return "✅ Birthday added."


@input_error
def show_birthday(book: AddressBook) -> str:
    """
    Shows the birthday of the contact with the given name in the `book`.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the birthday of the contact with the given
        name.
    """
    name = input("Enter name: ")

    record = book.find(name)
    return f"🎂 Birthday: {record.birthday}"


@input_error
def birthdays(book: AddressBook) -> str:
    """
    Returns a string containing the names and congratulation dates of all
    contacts in the `book` who have a birthday within the next 7 days.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the names and congratulation dates of all
        contacts in the `book` who have a birthday within the next 7 days.
    """
    return "\n".join([str(record) for record in book.get_upcoming_birthdays()])
