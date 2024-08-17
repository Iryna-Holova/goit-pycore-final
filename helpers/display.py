import re
import textwrap
from tabulate import tabulate

from contacts.address_book import AddressBook
from contacts.record import Record
from notes.notes_book import NotesBook
from notes.note import Note
from helpers.colors import blue, green, yellow, warning


def wrap_text(text, width=20):
    return "\n".join(textwrap.wrap(str(text), width=width))


def display_contacts(book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."

    headers = ["Name", "Phones", "Birthday", "Email", "Address"]
    colored_headers = [blue(header) for header in headers]
    table = []
    for contact in book.data.values():
        phones_str = " ".join(map(str, contact.phones)) if contact.phones else " - "
        address = getattr(contact, "address", None)
        table.append(
            [
                str(contact.name),
                wrap_text(phones_str),
                str(contact.birthday) if contact.birthday else " - ",
                str(contact.email) if contact.email else " - ",
                wrap_text(str(address)) if address else " - ",
            ]
        )

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")

    return table_str


def highlight_term(text: str, term: str, bg_color_code: str = "\033[43m") -> str:
    """
    Highlights the term in the text by changing the background color.
    Args:
        text (str): The text to search in.
        term (str): The term to highlight.
        bg_color_code (str): The ANSI background color code to use for
        highlighting
            (default is yellow).
    Returns:
        str: The text with the term highlighted with a background color.
    """
    term = re.escape(term)
    highlighted_text = re.sub(
        f'({term})',
        f'{bg_color_code}\\1\033[0m',
        text,
        flags=re.IGNORECASE
    )
    return highlighted_text



def display_contact(contact: Record, search_term: str = '') -> str:
    headers = ["Name", "Phones", "Birthday", "Address"]
    colored_headers = [green(header) for header in headers]
    # Highlight the search term in the name
    name_str = str(contact.name)
    if search_term:
        name_str = highlight_term(name_str, search_term)

    # Highlight the search term in phone numbers
    phones_str = (
        " ".join([highlight_term(str(phone), search_term) for phone in contact.phones])
        if contact.phones
        else " - "
    )

    table = [
        [
            name_str,
            phones_str,
            str(contact.birthday) if contact.birthday else " - ",
            str(contact.email) if contact.email else " - ",
            str(contact.address) if contact.address else " - ",
        ]
    ]

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")
    return table_str


def display_notes(book: NotesBook) -> str:
    if not book.data:
        return "Notes book is empty."

    headers = ["Title", "Text", "Tags", "Created On", "Reminder"]
    colored_headers = [blue(header) for header in headers]
    table = []
    for note in book.data.values():
        tags_str = (", ".join([f"#{tag}" for tag in note.tags])
                    if note.tags else " - ")
        reminder_str = str(note.reminder) if note.reminder else " - "
        table.append([
            str(note.title),
            wrap_text(note.text),
            wrap_text(tags_str),
            str(note.created_on),
            reminder_str
        ])

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")
    return table_str


def display_note(note: Note) -> str:
    headers = ["Title", "Text", "Tags", "Created On", "Reminder"]
    colored_headers = [green(header) for header in headers]
    tags_str = (", ".join([f"#{tag}" for tag in note.tags])
                if note.tags else " - ")
    reminder_str = str(note.reminder) if note.reminder else " - "
    table = [[
        str(note.title),
        wrap_text(note.text),
        wrap_text(tags_str),
        str(note.created_on),
        reminder_str
    ]]

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")
    return table_str


def display_reminders(book: NotesBook, days: int) -> str:
    notes_with_reminders = book.upcoming_reminders(days)
    if not notes_with_reminders:
        return warning(f"No reminders in the next {days} days.")
    headers = ["Title", "Text", "Tags", "Created On", "Reminder"]
    colored_headers = [yellow(header) for header in headers]
    table = []
    for note in notes_with_reminders:
        tags_str = (", ".join([f"#{tag}" for tag in note.tags])
                    if note.tags else " - ")
        reminder_str = str(note.reminder) if note.reminder else " - "
        table.append([
            str(note.title),
            wrap_text(note.text),
            wrap_text(tags_str),
            str(note.created_on),
            reminder_str
        ])

    table_str = tabulate(table, headers=colored_headers, tablefmt="grid")
    return table_str
