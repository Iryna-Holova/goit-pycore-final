"""
Phone field module.
"""

import re

PHONE_REGEXP = r"^\d{10}$"


class Phone:
    """
    Class representing a phone field.
    """

    def __init__(self, phone: str) -> None:
        """
        Initialize a phone field.

        Args:
            phone (str): The phone number.

        Raises:
            ValueError: If the phone number does not consist of 10 digits.
        """
        if not re.match(PHONE_REGEXP, phone):
            raise ValueError("❌ Phone number must consist of 10 digits")
        self.value = phone

    def __str__(self) -> str:
        """
        Return the string representation of the phone field.

        Returns:
            str: The string representation of the phone field.
        """
        return self.value

    def __eq__(self, other) -> bool:
        """
        Checks if two Phone instances are equal.

        Args:
            other (Phone): The Phone instance to compare with.

        Returns:
            bool: True if the Phone instances are equal, False otherwise.
        """
        return isinstance(other, Phone) and self.value == other.value

