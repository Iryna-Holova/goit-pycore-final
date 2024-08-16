"""
Email field module.
"""

import re
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class Email:
    """
    Class representing an email field.
    """

    def __init__(self, email: str) -> None:
        """
        Initialize an address field.

        Args:
            address (str): The address.

        Raises:
            ValueError: If the address does not meet the validation criteria.
        """
        if not re.match(EMAIL_REGEX, email):
            raise ValueError("Invalid email address.")
        self.value = email

    def __str__(self) -> str:
        """
        Return the string representation of the address field.

        Returns:
            str: The string representation of the address field.
        """
        return self.value
