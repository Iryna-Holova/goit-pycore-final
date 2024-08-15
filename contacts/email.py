from helpers.colors import green, blue, warning, danger
from contacts.record import Record
from helpers.completer import Prompt

def add_emails(contact: Record) -> None:
    """
    Adds a new email address to the contact.

    Args:
        contact (Record): An instance of the Record class.

    Returns:
        None
    """
    while True:
        try:
            email = input(blue("Enter email address or press Enter to skip: "))
            if not email:
                break
            contact.add_email(email)
            print(green("Email address added."))
        except ValueError as e:
            print(danger(str(e)))
            continue

def remove_email(contact: Record) -> None:
    """
    Removes an email address from the contact.

    Args:
        contact (Record): An instance of the Record class.

    Returns:
        None
    """
    prompt = Prompt()
    while True:
        try:
            email = prompt.prompt(
                "Enter email address to remove or press Enter to skip: ",
                list(map(str, contact.emails)), True, style="cyan"
            )
            if not email:
                break
            contact.remove_email(email)
            print(green("Email address removed."))
        except ValueError as e:
            print(danger(str(e)))
            continue
