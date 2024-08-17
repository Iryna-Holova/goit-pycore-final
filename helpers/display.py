import textwrap
from tabulate import tabulate
from contacts.address_book import AddressBook
from contacts.record import Record
import re
from helpers.colors import blue, green, success


def wrap_text(text, width=20):
    return "\n".join(textwrap.wrap(text, width=width))


def display_contacts(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."

    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [blue(header) for header in headers]
    table = []
    for contact in book.data.values():
        phones_str = (" ".join(map(str, contact.phones))
                      if contact.phones else " - ")
        address = getattr(contact, 'address', None)
        table.append([
            str(contact.name),
            wrap_text(phones_str),
            str(contact.birthday) if contact.birthday else " - ",
            wrap_text(str(address)) if address else " - "
        ])

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")

    return table_str


def highlight_term(text: str, term: str, bg_color_code: str = "\033[43m") -> str:
    """
    Highlights the term in the text by changing the background color.
    
    Args:
        text (str): The text to search in.
        term (str): The term to highlight.
        bg_color_code (str): The ANSI background color code to use for highlighting (default is yellow).
    
    Returns:
        str: The text with the term highlighted with a background color.
    """
    term = re.escape(term)
    highlighted_text = re.sub(f'({term})', f'{bg_color_code}\\1\033[0m', text, flags=re.IGNORECASE)
    return highlighted_text


def display_contact(contact: Record, search_term: str = '') -> str:
    """
    Displays a single contact with the option to highlight the search term in the contact name and phones.
    
    Args:
        contact (Record): The contact to display.
        search_term (str): The search term to highlight (optional).
    
    Returns:
        str: The formatted contact string with highlighted term in the name and phones.
    """
    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [green(header) for header in headers]
    
    # Highlight the search term in the name
    name_str = str(contact.name)
    if search_term:
        name_str = highlight_term(name_str, search_term)
    
    # Highlight the search term in phone numbers
    phones_str = (" ".join(
        [highlight_term(str(phone), search_term) for phone in contact.phones]
    ) if contact.phones else " - ")
    
    table = [[
        name_str,
        phones_str,
        str(contact.birthday) if contact.birthday else " - ",
        str(contact.address) if contact.address else " - "
    ]]

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")
    return table_str
