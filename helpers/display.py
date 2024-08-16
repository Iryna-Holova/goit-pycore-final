import textwrap
from tabulate import tabulate
from contacts.address_book import AddressBook
from contacts.record import Record
from helpers.colors import blue, green


def wrap_text(text, width=20):
    return "\n".join(textwrap.wrap(text, width=width))

def display_contacts(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."

    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [blue(header) for header in headers]
    table = []
    for contact in book.data.values():
        phones_str = ", ".join(map(str, contact.phones)) if contact.phones else " * * * "
        address = getattr(contact, 'address', None)
        table.append([
            str(contact.name),
            wrap_text(phones_str),
            str(contact.birthday) if contact.birthday else " * * * ",
            wrap_text(str(address)) if address else " * * * "
        ])

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")

    return table_str

def display_contact(contact: Record) -> str:
    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [green(header) for header in headers]
    phones_str = ", ".join(map(str, contact.phones)) if contact.phones else " * * * "
    table = [[
        str(contact.name),
        phones_str,
        str(contact.birthday) if contact.birthday else " * * * ",
        str(contact.address) if contact.address else " * * * "
    ]]

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")

    return table_str
