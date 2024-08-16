"""
Main module.
"""

from helpers.suggest import suggest_command
from helpers.completer import Prompt
from helpers.serialize import save_data, load_data
from helpers.colors import green, danger, success
from helpers.help import get_help
from notes.notes_book import NotesBook
from controllers.notes_controllers import (
    add_note, add_text, add_tag, get_notes, change_note)
from controllers.contacts_controllers import (
    add_contact,
    change_contact,
    get_contacts,
    birthdays,
    delete_contact,
    fake_contacts,
    search_contacts,
)

controllers = {
    "add-contact": add_contact,
    "change-contact": change_contact,
    "delete-contact": delete_contact,
    "all-contacts": get_contacts,
    "birthdays": birthdays,
    "fake-contacts": fake_contacts,
    "help": get_help,
    "search-contacts": search_contacts,
}
notes_controllers = {
    "add-note": add_note,
    "add-text": add_text,
    "add-tag": add_tag,
    "all-notes": get_notes,
    "change-note": change_note,
}


def main():
    """
    The main function that serves as the entry point for the application.
    """
    book = load_data()
    notes_book = NotesBook()
    print(success("Welcome to the assistant bot!"))

    commands = list(controllers) + ["close", "exit"]
    prompt = Prompt()

    while True:
        try:
            command = prompt.prompt(
                "Enter a command: ", commands).strip().lower()
        except KeyboardInterrupt:
            print("Good bye!")
            save_data(book)
            break

        if not command:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        if command == "hello":
            print(green("How can I help you?"))

        elif command in controllers:
            print(controllers[command](book))

        elif command in notes_controllers:
            print(notes_controllers[command](notes_book))

        else:
            similar_commands = suggest_command(command, commands)
            print(danger("Invalid command."))
            if similar_commands and similar_commands != command:
                print("The most similar commands are")
                for cmd in similar_commands:
                    print(f"\t'{cmd}'")


if __name__ == "__main__":
    main()
