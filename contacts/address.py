"""
Address field module.
"""

import re

ADDRESS_REGEXP = r"^[\w\s.,-]{5,100}$" 

class Address:
    """
    Class representing an address field.
    """

    def __init__(self, address: str) -> None:
        """
        Initialize an address field.

        Args:
            address (str): The address.

        Raises:
            ValueError: If the address does not meet the validation criteria.
        """
        if not re.match(ADDRESS_REGEXP, address):
            raise ValueError("❌ Address must be between 5 and 100 characters long and contain only valid characters.")
        self.value = address

    def __str__(self) -> str:
        """
        Return the string representation of the address field.

        Returns:
            str: The string representation of the address field.
        """
        return self.value

    def __eq__(self, other) -> bool:
        """
        Checks if two Address instances are equal.

        Args:
            other (Address): The Address instance to compare with.

        Returns:
            bool: True if the Address instances are equal, False otherwise.
        """
        return isinstance(other, Address) and self.value == other.value
