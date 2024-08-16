"""
Serialize and deserialize address book data
"""

from rich.progress import Progress
from time import sleep
import pickle
from contacts.address_book import AddressBook


def save_data(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    """
    Saves the provided address book data to a file.

    Args:
        book (AddressBook): The address book data to be saved.
        filename (str, optional): The name of the file where the data will be
        saved. Defaults to "addressbook.pkl".

    Returns:
        None
    """
    with Progress() as progress:
        task = progress.add_task("[blue]Saving data to file...", total=100)
        while not progress.finished:
            progress.update(task, advance=100)
            sleep(0.8)
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = "addressbook.pkl") -> AddressBook:
    """
    Loads address book data from a file.

    Args:
        filename (str, optional): The name of the file where the data will be
        loaded from. Defaults to "addressbook.pkl".

    Returns:
        AddressBook: The loaded address book data, or a new AddressBook
        instance if the file is not found.
    """
    with Progress() as progress:
        task = progress.add_task("[blue]Loading data from file...", total=100)
        while not progress.finished:
            progress.update(task, advance=100)
            sleep(0.8)
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
