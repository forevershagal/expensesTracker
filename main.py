import json
import os

FILENAME = "expenses.json"

print("Приветствую вас в консольном приложении <Трекер расходов>")

if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as file:
        expenses = json.load(file)
    print(f"[Система] Данные успешно загружены! Найдено записей: {len(expenses)}")
else:
    expenses = []
    print("[Система] База данных не найдена. Создан новый пустой список.")

while True:
    print('\n-----ФУНКЦИИ-----')
    print('1. Добавление расхода')
    print('2. Вывод всех расходов')
    print('3. Подсчет всех расходов')
    print('4. Подсчет расходов по категории')
    print('5. Выход')

    try:
        user_choice = int(input('Введите желаемое действие: '))

        if user_choice == 1:
            inp_value = int(input('Введите сумму расхода: '))
            inp_category = input('Введите категорию товара: ')
            item = {"amount": inp_value, "category": inp_category}
            expenses.append(item)

            with open(FILENAME, "w", encoding="utf-8") as file:
                json.dump(expenses, file, indent=4, ensure_ascii=False)

            print(f"Успешно добавлено и сохранено: {inp_value} руб. на категорию {inp_category}")

        elif user_choice == 2:
            if len(expenses) == 0:
                print('Ваш список расходов пуст.')
            else:
                for i in range(len(expenses)):
                    print(f'{i + 1}. {expenses[i]["category"]}: {expenses[i]["amount"]} руб.')

        elif user_choice == 3:
            total_sum = sum([i["amount"] for i in expenses])
            print(f'Сумма всех расходов составляет: {total_sum} руб.')

        elif user_choice == 4:
            inp_choice_category = input('Введите вашу категорию: ')
            category_sum = 0

            for i in range(len(expenses)):
                if expenses[i]["category"] == inp_choice_category:
                    print(f'{i + 1}. {expenses[i]["category"]}: {expenses[i]["amount"]} руб.')
                    category_sum += expenses[i]["amount"]
            print(f'Итоговые расходы в категории {inp_choice_category}: {category_sum} руб.')

        elif user_choice == 5:
            print("До свидания!")
            break

        else:
            print("Пожалуйста, введите число строго от 1 до 5.")

    except ValueError:
        print('Ошибка ввода! Убедитесь, что вводите числовые значения.')