class Title:
    def _init_(self, value: str = "") -> None:
        if len(value.strip()) < 2:
            raise ValueError("Title must be at least 2 symbols")
        self.value = value
