from tracker import ExpenseTracker

def say_hello():
    print('\n-----ФУНКЦИИ-----')
    print('1. Добавление расхода')
    print('2. Подсчет всех расходов')
    print('3. Подсчет расходов по категории')
    print('4. Подсчет расходов за сегодня')
    print('5. Вывод всего списка расходов и статистики')
    print('6. Удаление расхода')
    print('7. Экспорт отчета в Excel')
    print('8. Аналитика и прогноз')
    print('9. Выход')

def display_analytics(analytics_data):
    print('\n===== КРАТКАЯ АНАЛИТИКА =====')
    print(f'Всего дней с нами: {analytics_data["total_days"]}')
    print(f'Средней чек одной покупки: {analytics_data["avg_check"]} руб.')
    print(f'Средний расход в день: {analytics_data["avg_per_days"]} руб.')
    print('=============================')


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
                display_analytics(tracker.get_analytics())
            elif user_choice == 6:
                index = int(input('Введите индекс товара в общем списке: '))
                if tracker.delete_expense(index):
                    print('Расход был успешно удален!')
                else:
                    print('[СИСТЕМА] Ошибка! Неверный индекс. Попробуйте еще раз')
            elif user_choice == 7:
                print('[СИСТЕМА] Формируем отчет...')
                if tracker.export_to_excel('expenses_report.xlsx'):
                    print('[СИСТЕМА] Отчет "expenses_report.xlsx" успешно создан в папке проекта')
                else:
                    print('[СИСТЕМА Ошибка! Не получилось создать отчет. (Возможно, список расходов пуст)')
            elif user_choice == 8:
                print('[СИСТЕМА] Просчитываем математическую модель тренда...')

                trend = tracker.get_trend_prediction()

                if trend is None:
                    print('[СИСТЕМА] Недостаточно данных для прогноза! Нужно вести трекер хотя бы 3 разных дня.')
                else:
                    print('\n===== ИНТЕЛЛЕКТУАЛЬНЫЙ ПРОГНОЗ =====')
                    print(f"Направление ваших трат: {trend['trend_direction']}")
                    print(f"Коэффициент скорости (скос): {trend['slope_k']}")
                    print(f"Математический прогноз на завтра: {trend['predicted_tomorrow']} руб.")
                    print(f"Ожидаемая сумма трат за следующий месяц: {trend['predicted_month_total']} руб.")
                    print('====================================')

            elif user_choice == 9:
                print('До свидания!')
                tracker.save_data()
                break
            else:
                print('[СИСТЕМА] Ошибка! Введите число от 1 до 8. Не больше и не меньше :)')
        except ValueError:
            print('[СИСТЕМА] Неверный тип ввода. Требуется цифра от 1 до 8. Попробуйте еще раз.')


if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    print("Приветствую вас в консольном приложении <Трекер расходов>")
    program(expense_tracker)

