from tracker import ExpenseTracker

def say_hello():
    print('\n-----ФУНКЦИИ-----')
    print('1. Добавление расхода')
    print('2. Подсчет всех расходов')
    print('3. Подсчет расходов по категории')
    print('4. Подсчет расходов за сегодня')
    print('5. Вывод всего списка расходов')
    print('6. Удаление расхода')
    print('7. Выход')

def display_expenses(expenses):
    if len(expenses) == 0:
        print('Список расходов еще пуст!')
    else:
        for i, item in enumerate(expenses):
            print(f'{i+1}. {item.category}: {item.amount} руб. Дата: {item.date}')

def program(tracker):
    while True:
        say_hello()
        try:
            user_choice = int(input('Введите номер программы: '))
            if user_choice == 1:
                inp_amount = int(input('Введите стоимость товара/услуги: '))
                inp_category = input('Введите категорию товара/услуги: ')
                tracker.add_expense(inp_amount, inp_category)
            elif user_choice == 2:
                total_sum = tracker.get_total()
                print(f'Сумма всех расходов составила: {total_sum}')
            elif user_choice == 3:
                inp_category = input('Введите категорию товара/услуги: ')
                total_sum_category = tracker.get_total_by_category(inp_category)
                print(f'Сумма расходов в категории {inp_category} составила: {total_sum_category}')
            elif user_choice == 4:
                total_sum = tracker.get_today_total()
                print(f'Сумма всех расходов за сегодня составила: {total_sum}')
            elif user_choice == 5:
                display_expenses(tracker.expenses)
            elif user_choice == 6:
                index = int(input('Введите индекс товара в общем списке: '))
                if tracker.delete_expense(index):
                    print('Расход был успешно удален!')
                else:
                    print('[СИСТЕМА] Ошибка! Неверный индекс. Попробуйте еще раз')
            elif user_choice == 7:
                print('До свидания!')
                tracker.save_data()
                break
            else:
                print('[СИСТЕМА] Ошибка! Введите число от 1 до 7. Не больше и не меньше :)')
        except ValueError:
            print('[СИСТЕМА] Неверный тип ввода. Требуется цифра от 1 до 7. Попробуйте еще раз.')


if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    print("Приветствую вас в консольном приложении <Трекер расходов>")
    program(expense_tracker)

