"""
Main module.
"""

from serialize import save_data, load_data
from cotrollers import (
    add_contact,
    change_contact,
    get_phones,
    get_contacts,
    add_birthday,
    show_birthday,
    birthdays,
)

controllers = {
    "add": add_contact,
    "change": change_contact,
    "phone": get_phones,
    "all": get_contacts,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
}


def main():
    """
    The main function that serves as the entry point for the application.
    """
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        if command == "hello":
            print("How can I help you?")

        elif command in controllers:
            print(controllers[command](book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
