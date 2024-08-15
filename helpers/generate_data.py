"""
Generate data module.
"""

import random
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
        "name": random.choice([fake.name(), fake.first_name()]),
        "phones": [
            "".join(random.choices("0123456789", k=10))
            for _ in range(random.randint(0, 4))
        ],
        "birthday": (
            fake.date_of_birth().strftime("%d.%m.%Y") if random.random() < 0.7 else ""
        ),
        "email": (fake.email() if random.random() < 0.7 else ""),
        "address": (
            f"{fake.street_address()}, {fake.city()}, {fake.state()}"
            if random.random() < 0.7
            else ""
        ),
    }

    return data
