"""
Address field module.
"""


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
        if len(address) < 5 or len(address) > 100:
            raise ValueError("Address must be between 5 and 100 characters.")
        self.value = address

    def __str__(self) -> str:
        """
        Return the string representation of the address field.

        Returns:
            str: The string representation of the address field.
        """
        return self.value
