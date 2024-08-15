import re

EMAIL_REGEXP = r"^[\w\.-]+@[\w\.-]+\.\w+$"

class Email:
    """
    Class representing an email field.
    """

    def __init__(self, email: str) -> None:
        """
        Initialize an email field.

        Args:
            email (str): The email address.

        Raises:
            ValueError: If the email address is not valid.
        """
        if not re.match(EMAIL_REGEXP, email):
            raise ValueError("❌ Invalid email address format")
        self.value = email

    def __str__(self) -> str:
        """
        Return the string representation of the email field.

        Returns:
            str: The string representation of the email field.
        """
        return self.value

    def __eq__(self, other) -> bool:
        """
        Checks if two Email instances are equal.

        Args:
            other (Email): The Email instance to compare with.

        Returns:
            bool: True if the Email instances are equal, False otherwise.
        """
        return isinstance(other, Email) and self.value == other.value
