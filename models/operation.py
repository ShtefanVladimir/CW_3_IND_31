from datetime import datetime


class Foo:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str
    ):
        self.pk = pk
        self.date = self.covert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.convert_payment(from_) if from_ else ""
        self.to = self.convert_payment(to)

    def convert_payment(self, payment: str) -> str:
        if payment.startswith("Счет"):
            ...
        else:
            ...
        return "XXXX XX** **** XXXX"

    def covert_date(self, date: str) -> datetime:
        return datetime.fromisoformat(date)

    def __str__(self):
        return (
            f"{datetime.strftime(self.date, '%d.%m.%Y')} Перевод организации \n"
            f"{self.from_} -> {self.to} \n"
            f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}."
        )