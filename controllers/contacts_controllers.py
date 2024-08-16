"""
Controllers module.

The controllers module contains functions that interact with the user and
modify the address book.
"""

from time import sleep
from rich.progress import Progress
from contacts.address_book import AddressBook
from contacts.record import Record
from helpers.colors import green, blue, success, warning, danger
from helpers.generate_data import generate_random_contact
from helpers.completer import Prompt
from helpers.display import display_contacts, display_contact


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
    try:
        while True:
            name = input(blue("Enter name: "))
            if name.strip().lower() in book.data:
                print(warning("Contact already exists."))
                continue
            try:
                new_record = Record(name)
                break
            except ValueError as e:
                print(danger(str(e)))
                continue

        add_phones(new_record)
        edit_birthday(new_record)
        edit_address(new_record)
        book.add_record(new_record)
        print(display_contact(new_record))
        return success("Contact was added.")
    except KeyboardInterrupt:
        return danger("\nOperation canceled.")


def change_contact(book: AddressBook) -> str:
    """
    Edits an existing contact in the `book`.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A message indicating whether the contact was edited or not.
    """
    is_edited = False
    prompt = Prompt()
    try:
        while True:
            name = prompt.prompt("Enter name: ", list(book))
            try:
                contact = book.find(name)
                break
            except ValueError as e:
                print(danger(str(e)))
                continue

        print(contact)
        while True:
            commands = {
                "add-phones": add_phones,
            }
            if contact.phones:
                commands["remove-phones"] = remove_phone
            if contact.birthday:
                commands["remove-birthday"] = contact.remove_birthday
                commands["edit-birthday"] = edit_birthday
            else:
                commands["add-birthday"] = edit_birthday
            if contact.email:
                commands["remove-email"] = contact.remove_email
                commands["edit-email"] = edit_email
            else:
                commands["add-email"] = edit_email
            if contact.address:
                commands["remove-address"] = contact.remove_address
                commands["edit-address"] = edit_address
            else:
                commands["add-address"] = edit_address
            print(
                green(
                    f"Choose a command: {", ".join(list(commands))}"
                )
            )
            command = prompt.prompt(
                "Enter a command or press Enter to quit: ", list(commands)
            )
            if not command:
                break
            if command in commands:
                commands[command](contact)
                is_edited = True
                print(contact)
            else:
                print(danger("Invalid command."))
                continue
        return (
            success("Contact was edited.")
            if is_edited
            else danger("\nOperation canceled.")
        )
    except KeyboardInterrupt:
        return (
            success("Contact was edited.")
            if is_edited
            else danger("\nOperation canceled.")
        )


def add_phones(contact: Record) -> None:
    """
    Adds a new phone number to the `contact`.

    Args:
        contact (Record): An instance of the `Record` class.

    Returns:
        None
    """
    while True:
        try:
            phone = input(blue("Enter phone number or press Enter to skip: "))
            if not phone:
                break
            contact.add_phone(phone)
            print(green("Phone number added."))
        except ValueError as e:
            print(danger(str(e)))
            continue


def remove_phone(contact: Record) -> None:
    """
    Removes a phone number from the `contact`.

    Args:
        contact (Record): An instance of the `Record` class.

    Returns:
        None
    """
    prompt = Prompt()
    while True:
        try:
            phone = prompt.prompt(
                "Enter phone number or press Enter to skip: ",
                list(map(str, contact.phones)),
                True,
                style="cyan",
            )
            if not phone:
                break
            contact.remove_phone(phone)
            print(green("Phone number removed."))
        except ValueError as e:
            print(danger(str(e)))
            continue


def edit_birthday(contact: Record) -> None:
    """
    Edits the birthday of the `contact`.

    Args:
        contact (Record): An instance of the `Record` class.

    Returns:
        None
    """
    while True:
        try:
            birthday = input(blue("Enter birthday or press Enter to skip: "))
            if not birthday:
                break
            contact.add_birthday(birthday)
            print(green("Birthday added."))
            break
        except ValueError as e:
            print(danger(str(e)))
            continue


def edit_address(contact: Record) -> None:
    """
    Edits the address of the `contact`.

    Args:
        contact (Record): An instance of the `Record` class.

    Returns:
        None
    """
    while True:
        try:
            address = input(blue("Enter address or press Enter to skip: "))
            if not address:
                break
            contact.add_address(address)
            print(green("Address added."))
            break
        except ValueError as e:
            print(danger(str(e)))
            continue


def edit_email(contact: Record) -> None:
    """
    Edits the email of the `contact`.

    Args:
        contact (Record): An instance of the `Record` class.

    Returns:
        None
    """
    while True:
        try:
            email = input(blue("Enter email or press Enter to skip: "))
            if not email:
                break
            contact.add_email(email)
            print(green("Email added."))
            break
        except ValueError as e:
            print(danger(str(e)))
            continue


def delete_contact(book: AddressBook) -> str:
    """
    Deletes a contact from the address book.

    Args:
        book (AddressBook): An instance of the AddressBook class from which
        the contact will be deleted.

    Returns:
        str: A success message indicating the deletion of the contact.
    """
    prompt = Prompt()
    while True:
        try:
            name = prompt.prompt("Enter name: ", list(book))
            book.delete(name)
            break
        except ValueError as error:
            print(warning(str(error)))
        except KeyboardInterrupt:
            return danger("Operation canceled.")
    return success(f"Contact {name} deleted.")


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
    with Progress() as progress:
        task = progress.add_task("[blue]Processing...", total=100)

        while not progress.finished:
            progress.update(task, advance=100)
            sleep(0.8)

    if not book.data:
        return warning("Address book is empty.")

    return display_contacts(book)


# @input_error
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
    while True:
        days = input(blue("Enter number of days: "))
        if not days.isdigit():
            print(warning("Invalid input. Please enter a valid number."))
            continue
        return book.upcoming_birthdays(int(days))


def fake_contacts(book: AddressBook) -> str:
    """
    Generates a specified number of fake contacts and adds them to the address
    book.

    Args:
        book (AddressBook): An instance of the AddressBook class to which the
        fake contacts will be added.

    Returns:
        str: A success message indicating the number of fake contacts added.
    """
    while True:
        try:
            count = input(blue("Enter number of fake contacts: "))
            if not count.isdigit():
                print(warning("Invalid input. Please enter a valid number."))
                continue
            count = int(count)
            break
        except KeyboardInterrupt:
            return danger("\nOperation canceled.")

    for _ in range(count):
        contact = generate_random_contact()
        record = Record(contact["name"])
        for phone in contact["phones"]:
            record.add_phone(phone)
        if contact["birthday"]:
            record.add_birthday(contact["birthday"])
        if contact["address"]:
            record.add_address(contact["address"])
        book.add_record(record)

    return success(f"{count} fake contacts added.")


def search_contacts(book: AddressBook) -> str:
    """
    Searches for contacts in the `book` that match the given search term.

    Args:
        book (AddressBook): An instance of the `AddressBook` class.

    Returns:
        str: A string containing the names and phone numbers of all contacts
        in the `book` that match the given search term.
    """
    while True:
        search_term = input(blue("Enter search term (name or phone number): "))
        if search_term.lower() == "q":
            return danger("Operation canceled.")
        if not search_term:
            print(
                warning("Invalid input. Please enter a valid search term or q to exit")
            )
            continue

        results = book.search(search_term)
        if results:
            return "\n".join([display_contact(contact) for contact in results])
        return warning("No contacts found matching the search term.")
