from colorama import Fore, Style

def get_help(_) -> str:
    """
    Returns a help message with list of available commands.
    """
    message = f"""
    {Fore.CYAN}Available commands:
    - hello: Displays a welcome message.
    - help: Shows this help message.
    - add-contact: Starts the flow for adding new contact.
                        Will ask for name, phone(s), birthday, address.
    - change-contact: Open submenu with commands to change contact:
        - add-phone: Add new phone
        - remove-phone: Remove phone
        - add-birthday: Change birthday
        - add-address: Add address
    - delete-contact: Delete contact by name
    - all-contacts: Shows all contacts with their phone numbers.
    - birthdays: Shows upcoming birthdays within the next 7 days.
    - fake-contacts: Debug function for generating dummy contacts,
    - search-contacts: Allows you to search for contacts by name or phone number.
    - smart-search: Interactive search with autocomplete suggestions during input.

    - close / exit : Exits the program.{Style.RESET_ALL}
    """
    return message
