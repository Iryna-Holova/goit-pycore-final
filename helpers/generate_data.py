"""
Generate data module.
"""

from random import randint, random, choice, choices
from faker import Faker


def generate_random_contact() -> dict:
    """
    Generates a dictionary of random contact data.

    Returns:
        dict: A dictionary containing random contact data, including name,
        phones, birthday, email, and address.
    """
    fake = Faker()

    data = {
        "name": choice([fake.name(), fake.first_name()]),
        "phones": [
            "".join(choices("0123456789", k=10))
            for _ in range(randint(0, 4))
        ],
        "birthday": (
            fake.date_of_birth().strftime("%d.%m.%Y") if random() < 0.7 else ""
        ),
        "email": (fake.email() if random() < 0.7 else ""),
        "address": (
            f"{fake.street_address()}, {fake.city()}, {fake.state()}"
            if random() < 0.7
            else ""
        ),
    }

    return data
