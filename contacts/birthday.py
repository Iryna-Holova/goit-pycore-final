"""
Birthday field module.
"""

from datetime import datetime


class Birthday:
    """
    Class representing a birthday field.
    """

    def __init__(self, value: str) -> None:
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y").date()
            self.value = birthday
        except ValueError as exc:
            raise ValueError("❌ Invalid date format. Use DD.MM.YYYY") from exc

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")
