from datetime import datetime, timedelta


class Reminder:
    def __init__(self, remind_date) -> None:
        remind_datetime = datetime.strptime(remind_date, "%d.%m.%Y")
        if remind_datetime <= datetime.now():
            raise ValueError("Data must be greater than today")
        self.value = remind_datetime

    def set_reminder(self, new_date: str) -> None:
        remind_datetime = datetime.strptime(new_date, "%d.%m.%Y")
        if remind_datetime <= datetime.now():
            raise ValueError("Data must be greater than today")
        self.value = remind_datetime

    def is_reminder_due(self, days) -> bool:
        today = datetime.now()
        end_date = today + timedelta(days=days)

        return today <= self.value <= end_date

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")
