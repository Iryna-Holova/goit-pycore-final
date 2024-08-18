from colorama import Fore, Style

def get_help(_) -> str:
    """
    Returns a help message with list of available commands.
    """
    message = f"""
    {Fore.LIGHTGREEN_EX}Available commands:
    - {Fore.WHITE}{Style.BRIGHT}hello{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Displays a welcome message.
    - {Fore.WHITE}{Style.BRIGHT}help{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Shows this help message.
    - {Fore.WHITE}{Style.BRIGHT}add-contact{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Starts the process of adding a new contact.
                        Will ask for name, phone(s), birthday, email, and address.
    - {Fore.WHITE}{Style.BRIGHT}change-contact{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Opens a submenu with commands to change a contact:
        - {Fore.WHITE}{Style.BRIGHT}add-phones{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Adds a new phone.
        - {Fore.WHITE}{Style.BRIGHT}remove-phones{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Removes phone.
        - {Fore.WHITE}{Style.BRIGHT}add-birthday{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Adds a birthday.
        - {Fore.WHITE}{Style.BRIGHT}edit-birthday{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Edits the birthday.
        - {Fore.WHITE}{Style.BRIGHT}remove-birthday{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Removes the birthday.
        - {Fore.WHITE}{Style.BRIGHT}add-email{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Adds an email.
        - {Fore.WHITE}{Style.BRIGHT}edit-email{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Edits the email.
        - {Fore.WHITE}{Style.BRIGHT}remove-email{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Removes the email.
        - {Fore.WHITE}{Style.BRIGHT}add-address{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Adds an address.
        - {Fore.WHITE}{Style.BRIGHT}edit-address{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Edits the address.
        - {Fore.WHITE}{Style.BRIGHT}remove-address{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Removes the address.
    - {Fore.WHITE}{Style.BRIGHT}delete-contact{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Deletes a contact by name.
    - {Fore.WHITE}{Style.BRIGHT}all-contacts{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Shows all contacts with their phone numbers.
    - {Fore.WHITE}{Style.BRIGHT}birthdays{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Shows upcoming birthdays within the next 7 days.
    - {Fore.WHITE}{Style.BRIGHT}fake-contacts{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Generates a specified number of fake contacts and adds them to an address book.
    - {Fore.WHITE}{Style.BRIGHT}search-contacts{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Allows you to search for contacts by name or phone number.
    - {Fore.WHITE}{Style.BRIGHT}smart-search{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Interactive search with autocomplete suggestions during input.
    - {Fore.WHITE}{Style.BRIGHT}add-note{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Starts the process of adding a new note to the notebook.
                        Will ask for text, tag(s), reminder.
    - {Fore.WHITE}{Style.BRIGHT}change-note{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Opens a submenu with commands to change the note: 
        - {Fore.WHITE}{Style.BRIGHT}edit-text{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Edits the text of the note.
        - {Fore.WHITE}{Style.BRIGHT}add-tags{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Adds a tag to the note.
        - {Fore.WHITE}{Style.BRIGHT}remove-tag{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Removes the tag from the note.
        - {Fore.WHITE}{Style.BRIGHT}add-reminder{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}:  Adds a reminder to the note.
    - {Fore.WHITE}{Style.BRIGHT}delete-note{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Deletes a note from the notebook.
    - {Fore.WHITE}{Style.BRIGHT}all-notes{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Shows all notes in the notebook.
    - {Fore.WHITE}{Style.BRIGHT}fake-notes{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Generates a specified number of fake notes and adds them to the notebook.
    - {Fore.WHITE}{Style.BRIGHT}reminders{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Shows reminders within the next specified number of days.

    - {Fore.WHITE}{Style.BRIGHT}close / exit{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}: Exits the program.{Style.RESET_ALL}
    """
    return message
