"""
Name field module.
"""


class Name:
    """
    Class representing a name field.
    """

    def __init__(self, contact_name: str) -> None:
        """
        Initialize a name field.

        Args:
            contact_name (str): The name of the contact.

        Raises:
            ValueError: If the contact name is empty.
        """
        if not contact_name.strip():
            raise ValueError("❌ Name cannot be empty")
        self.value = contact_name

    def __str__(self) -> str:
        """
        Return the string representation of the name field.

        Returns:
            str: The string representation of the name field.
        """
        return self.value
