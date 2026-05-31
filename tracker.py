from datetime import datetime
from dataclasses import asdict
import os
import json
from models import Expense


class ExpenseTracker:
    def __init__(self):
        self.filename = "expenses.json"
        self.expenses = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                expenses = json.load(file)
                print(f"[Система] Данные успешно загружены! Найдено записей: {len(expenses)}")
                return [Expense(item["amount"], item["category"], item.get("date", "Дата не указана")) for item in expenses]
        else:
            print("[Система] База данных не найдена. Создан новый пустой список.")
            return []


    def save_data(self):
        with open(self.filename, 'w', encoding="utf-8") as file:
            ready_to_save = [asdict(item) for item in self.expenses]
            json.dump(ready_to_save, file, indent=4, ensure_ascii=False)

    def add_expense(self, amount, category):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        item = Expense(amount, category, current_time)
        self.expenses.append(item)
        self.save_data()
        return item

    def delete_expense(self, index):
        if index <= 0:
            return False
        try:
            self.expenses.pop(index-1)
            self.save_data()
            return True
        except IndexError:
            return False

    def get_total(self):
        return sum(item.amount for item in self.expenses)

    def get_total_by_category(self, category):
        return sum(item.amount for item in self.expenses if item.category == category)

    def get_today_total(self):
        today_str = datetime.now().strftime("%Y-%m-%d")
        return sum(item.amount for item in self.expenses if item.date.startswith(today_str))


