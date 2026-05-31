from dataclasses import dataclass

@dataclass
class Expense:
    amount: int
    category: str
    date: str = ""
