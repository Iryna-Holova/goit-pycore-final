from title import Title
from remainder import Reminder
from created_on import CreatedOn


class Note:
    def __init__(self, title: str) -> None:
        self.title = Title(title)
        self.text = ""
        self.tags = []
        self.created_on = CreatedOn()
        self.reminder: Reminder | None = None

    def add_text(self, text: str) -> None:
        if len(text) > 200 or len(text) < 4:
            raise ValueError(
                "Text must contain min 4 symbols and max 200 symbols")
        self.text = text.strip()

    def add_tag(self, tag: str) -> None:
        tag = tag.strip()
        if len(tag) < 2:
            raise ValueError("Tag must contain at least 2 symbols")
        if tag not in self.tags:
            self.tags.append(tag)

    def set_reminder(self, remind_date: str) -> None:
        self.reminder = Reminder(remind_date)

    def __str__(self) -> str:
        pass
