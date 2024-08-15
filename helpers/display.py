from tabulate import tabulate
from contacts.address_book import AddressBook
from contacts.record import Record
from helpers.colors import blue, green

def display_contacts(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."

    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [blue(header) for header in headers]
    table = []
    for contact in book.data.values():
        phones_str = ", ".join(map(str, contact.phones)) if contact.phones else "N/A"
        address = getattr(contact, 'address', None)
        table.append([
            str(contact.name),
            phones_str,
            str(contact.birthday) if contact.birthday else "N/A",
            str(address) if address else "N/A"
        ])

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")

    return table_str

def display_contact(contact: Record) -> str:
    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [green(header) for header in headers]
    phones_str = ", ".join(map(str, contact.phones)) if contact.phones else "N/A"
    table = [[
        str(contact.name),
        phones_str,
        str(contact.birthday) if contact.birthday else "N/A",
        str(contact.address) if contact.address else "N/A"
    ]]

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")

    return table_str
