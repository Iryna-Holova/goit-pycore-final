"""
Note module.
"""

from typing import List
from notes.title import Title
from notes.tag import Tag
from notes.remainder import Reminder
from notes.created_on import CreatedOn


class Note:
    """
    Class representing a note in the notes book.

    Attributes:
        title (Title): The title of the note.
        text (str): The text of the note.
        tags (List[Tag]): The list of tags in the note.
        created_on (CreatedOn): The created_on of the note.
        reminder (Reminder): The reminder of the note.
    """

    def __init__(self, title: str) -> None:
        """
        Initializes a new Note instance.

        Args:
            title (str): The title of the note.

        Returns:
            None
        """
        self.title = Title(title)
        self.text = ""
        self.tags: List[Tag] = []
        self.created_on = CreatedOn()
        self.reminder: Reminder | None = None

    def add_text(self, text: str) -> None:
        """
        Adds text to the note.

        Args:
            text (str): The text to add.

        Returns:
            None

        Raises:
            ValueError: If the text contains lower than 4 symbols and greater than 200 symbols.
        """
        if len(text) > 200 or len(text) < 4:
            raise ValueError(
                "Text must contains min 4 symbols and max 200 symbols")
        self.text = text.strip()

    def add_tag(self, tag: str) -> None:
        """
        Adds tag to the note.

        Args:
            tag (str): The tag to add.

        Returns:
            None
        """
        tag_normalize_val = tag.strip().lower()
        if tag not in self.tags:
            self.tags.append(Tag(tag_normalize_val))

    def remove_tag(self, tag: str):
        """
        Removes a tag from the list of tags in the `Note`
        instance.

        Args:
            tag (str): The tag to remove.

        Raises:
            ValueError: If the tag is not found in the list of tags.

        Returns:
            None
        """
        tag_to_remove = Tag(tag)
        if tag_to_remove in self.tags:
            self.tags.remove(tag)
        else:
            raise ValueError(f"Tag {tag} not found")

    def set_reminder(self, remind_date: str) -> None:
        """
        Sets reminder to the note.

        Args:
            remind_date (str): The remind_date to add.

        Returns:
            None
        """
        self.reminder = Reminder(remind_date)

    def __str__(self):
        tags_str = ", ".join(map(str, self.tags)) if self.tags else ""
        """
        Returns a string containing the title, text, tags, created_on, reminder of note.

        Returns:
        str: A string containing title, text, tags, created_on, reminder of note.
        """
        return (
            f"title: {self.title}\n"
            f"text: {self.text}\n"
            f"tags: {tags_str}\n"
            f"created_on: {self.created_on}\n"
            f"reminder: {self.reminder}"

        )
