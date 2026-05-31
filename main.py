import json
import os


class ExpenseTracker:
    def __init__(self):
        self.filename = "expences.json"
        self.expenses = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                expenses = json.load(file)
                print(f"[Система] Данные успешно загружены! Найдено записей: {len(expenses)}")
                return expenses
        else:
            print("[Система] База данных не найдена. Создан новый пустой список.")
            return []

    def say_hello(self):
        print('\n-----ФУНКЦИИ-----')
        print('1. Добавление расхода')
        print('2. Подсчет всех расходов')
        print('3. Выход')

    def save_data(self):
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(self.expenses, file, indent=4, ensure_ascii=False)

    def add_expense(self, amount, category):
        item = {"amount": amount, "category": category}
        self.expenses.append(item)
        self.save_data()
        print(f'Расход {amount} руб. в категории {category} добавлен!')

    def get_total(self):
        return sum(item["amount"] for item in self.expenses)

    def program(self):
        while True:
            self.say_hello()
            try:
                user_choice = int(input('Введите номер программы: '))
                if user_choice == 1:
                    inp_amount = int(input('Введите стоимость товара/услуги: '))
                    inp_category = input('Введите категорию товара/услуги: ')
                    self.add_expense(inp_amount, inp_category)
                elif user_choice == 2:
                    total_sum = self.get_total()
                    print(f'Сумма всех расходов составила: {total_sum}')
                elif user_choice == 3:
                    print('До свидания!')
                    self.save_data()
                    break
                else:
                    print('[СИСТЕМА] Ошибка! Введите число от 1 до 3. Не больше и не меньше :)')
            except ValueError:
                print('[СИСТЕМА] Неверный тип ввода. Требуется цифра от 1 до 3. Попробуйте еще раз.')



if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    print("Приветствую вас в консольном приложении <Трекер расходов>")
    expense_tracker.program()

