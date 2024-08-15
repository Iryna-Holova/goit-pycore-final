from datetime import datetime


class CreatedOn:
    def __init__(self) -> None:
        self.created_on = datetime.now()

    def __str__(self) -> str:
        return self.created_on.strftime("%Y-%m-%d %H:%M:%S")
