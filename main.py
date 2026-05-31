from dataclasses import dataclass, asdict
import json
import os

@dataclass
class Expense:
    amount: int
    category: str

class ExpenseTracker:
    def __init__(self):
        self.filename = "expenses.json"
        self.expenses = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                expenses = json.load(file)
                print(f"[Система] Данные успешно загружены! Найдено записей: {len(expenses)}")
                return [Expense(item["amount"], item["category"]) for item in expenses]
        else:
            print("[Система] База данных не найдена. Создан новый пустой список.")
            return []

    def say_hello(self):
        print('\n-----ФУНКЦИИ-----')
        print('1. Добавление расхода')
        print('2. Подсчет всех расходов')
        print('3. Подсчет расходов по категории')
        print('4. Вывод всего списка расходов')
        print('5. Удаление расхода')
        print('6. Выход')

    def save_data(self):
        with open(self.filename, 'w', encoding="utf-8") as file:
            ready_to_save = [asdict(item) for item in self.expenses]
            json.dump(ready_to_save, file, indent=4, ensure_ascii=False)

    def add_expense(self, amount, category):
        item = Expense(amount, category)
        self.expenses.append(item)
        self.save_data()
        print(f'Расход {amount} руб. в категории {category} добавлен!')

    def print_all_expenses(self):
        if len(self.expenses) == 0:
            print('Список расходов еще пуст!')
        else:
            for i in range(len(self.expenses)):
                print(f'{i+1}. {self.expenses[i].category}: {self.expenses[i].amount} руб.')

    def delete_expense(self, index):
        try:
            if index > 0:
                self.expenses.pop(index-1)
                print('Расход был успешно удален')
                self.save_data()
            else:
                print('Значение индекса должно быть больше 0')
        except IndexError:
            print('Расхода с таким индексом не нашлось. Попробуйте еще раз')

    def get_total(self):
        return sum(item.amount for item in self.expenses)

    def get_total_by_category(self, category):
        return sum(item.amount for item in self.expenses if item.category == category)


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
                    inp_category = input('Введите категорию товара/услуги: ')
                    total_sum_category = self.get_total_by_category(inp_category)
                    print(f'Сумма расходов в категории {inp_category} составила: {total_sum_category}')
                elif user_choice == 4:
                    self.print_all_expenses()
                elif user_choice == 5:
                    index = int(input('Введите индекс товара в общем списке: '))
                    self.delete_expense(index)
                elif user_choice == 6:
                    print('До свидания!')
                    self.save_data()
                    break
                else:
                    print('[СИСТЕМА] Ошибка! Введите число от 1 до 6. Не больше и не меньше :)')
            except ValueError:
                print('[СИСТЕМА] Неверный тип ввода. Требуется цифра от 1 до 6. Попробуйте еще раз.')



if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    print("Приветствую вас в консольном приложении <Трекер расходов>")
    expense_tracker.program()

