"""
Controllers module.

The controllers module contains functions that interact with the user and
modify the notes book.
"""

from helpers.colors import green, blue, success, warning, danger
from prompt_toolkit import PromptSession
from helpers.completer import CustomCompleter
from notes.notes_book import NotesBook
from notes.note import Note


def add_note(book: NotesBook) -> str:
    """
    Adds a new note to the `book'.

    Args:
        book (NotesBook): An instance of the `NotesBook` class.

    Returns:
        str: A message indicating whether the note was added or
        if the input is invalid.
    """
    try:
        while True:
            title = input(blue("Enter title: "))
            if title.strip().lower() in book.data:
                print(warning("Note already exists."))
                continue
            try:
                new_note = Note(title)
                break
            except ValueError as e:
                print(danger(str(e)))
        add_text(new_note)
        add_tag(new_note)
        book.add_note(new_note)
        return str(title) + success("Note was added.")
    except KeyboardInterrupt:
        return danger("\nOperation canceled.")


def change_note(book: NotesBook) -> str:
    """
    Edits an existing note in the `notes book`.

    Args:
        book (NotesBook): An instance of the `NotesBook` class.

    Returns:
        str: A message indicating whether the note was edited or not.
    """
    is_edited = False
    session = PromptSession()
    try:
        while True:
            title = session.prompt(
                "Enter title: ",
                completer=CustomCompleter(list(book)),
                mouse_support=True,
            )
            try:
                note = book.find(title)
                break
            except ValueError as e:
                print(danger(str(e)))
                continue

        print(note)
        while True:
            commands = {
                "edit-text": edit_text,
                "add-tag": add_tag,
                "add-reminder": add_reminder,
                "remove-tag": remove_tag,
            }
            print(
                green(
                    "Choose a command: add-tag, remove-tag, "
                    "add-reminder, edit-text"
                )
            )
            command = session.prompt(
                "Enter a command or press Enter to quit: ",
                completer=CustomCompleter(list(commands)),
                mouse_support=True,
            )
            if not command:
                break
            if command in commands:
                commands[command](note)
                is_edited = True
                print(note)
            else:
                print(danger("Invalid command."))
                continue
        return (
            success("Note was edited.")
            if is_edited
            else danger("\nOperation canceled.")
        )
    except KeyboardInterrupt:
        return (
            success("Note was edited.")
            if is_edited
            else danger("\nOperation canceled.")
        )


def add_text(note: Note) -> None:
    """
    Adds text to the `note`.

    Args:
        note (Note): An instance of the `Note` class.

    Returns:
        None
    """
    while True:
        try:
            text = input(blue("Enter text or press Enter to skip: "))
            if not text:
                break
            note.add_text(text)
            print(green("Text added."))
        except ValueError as e:
            print(danger(str(e)))
            continue


def add_tag(note: Note) -> None:
    """
    Adds tag to the `note`.

    Args:
        note (Note): An instance of the `Note` class.

    Returns:
        None
    """
    while True:
        try:
            tag = input(blue("Enter tag or press Enter to skip: "))
            if not tag:
                break
            note.add_tag(tag)
            print(green("Tag added."))
        except ValueError as e:
            print(danger(str(e)))
            continue


def get_notes(book: NotesBook) -> str:
    """
    f"title: {self.title}\n"
            f"text: {self.text}\n"
            f"tags: {tags_str}\n"
            f"created_on: {self.created_on}\n"
            f"reminder: {self.reminder}"

    Returns a string containing the title, text, tags, created_on, reminder of all notes
    in the `book`.

    Args:
        book (NotesBook): An instance of the `NotesBook` class.

    Returns:
        str: A string containing title, text, tags, created_on, reminder of all notes
        in the `book`.
    """

    if not book.data:
        return warning("Notes book is empty.")

    return "\n".join(map(str, book.data.values()))


def edit_text(note: Note) -> None:
    """
    Edits the text of the `note`.

    Args:
        note (Note): An instance of the `Note` class.

    Returns:
        None
    """
    while True:
        try:
            text = input(blue("Enter text or press Enter to skip: "))
            if not text:
                break
            note.add_text(text)
            print(green("Text edited."))
            break
        except ValueError as e:
            print(danger(str(e)))
            continue


def remove_tag(note: Note) -> None:
    """
    Delete the tag of the `note`.

    Args:
        note (Note): An instance of the `Note` class.
        tag (str): An instance of the `str` class.

    Returns:
        None
    """
    while True:
        try:
            tag = input(blue("Enter tag or press Enter to skip: "))
            if not tag:
                break
            note.remove_tag(tag)
            print(green("Tag deleted."))
            break
        except ValueError as e:
            print(danger(str(e)))
            continue


def add_reminder(note: Note) -> None:
    """
    Adds a reminder to the note.

    Args:
        note (Note): An instance of the `Note` class.

    Returns:
        str: A message indicating whether the reminder was added or
        if the input is invalid.
    """
    while True:
        try:
            reminder = input(blue("Enter date or press Enter to skip: "))
            if not reminder:
                break
            note.set_reminder(reminder)
            print(green("Reminder added."))
        except ValueError as e:
            print(danger(str(e)))
            continue
