expenses = []
total_sum = 0
category_sum = 0
print("Приветствую вас в консольном приложении <Трекер расходов>")
while True:
    print('-----ФУНКЦИИ-----')
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
            item = {"amount": inp_value, "category": inp_category }
            expenses.append(item)
            print(f"Успешно добавлено: {inp_value} руб. на категорию {inp_category}")
        elif user_choice == 2:
            if len(expenses) == 0:
                print('Ваш список расходов пуст.')
            else:
                for i in range(len(expenses)):
                    print(f'{i + 1}. {expenses[i]["category"]}: {expenses[i]["amount"]} руб.')
        elif user_choice == 3:
            total_sum += sum([i["amount"] for i in expenses])
            print(f'Сумма всех расходов составляет: {total_sum}')
        elif user_choice == 4:
            inp_choice_category = print('Введите вашу категорию: ')
            for i in range(len(expenses)):
                if expenses[i]["category"] == inp_choice_category:
                    print(f'{i+1}. {expenses[i]["category"]}: {expenses[i]["amount"]}')
                    category_sum += expenses[i]["amount"]
            print(f'Итоговые расходы в категории {inp_choice_category}: {category_sum}')
        elif user_choice == 5:
            break
    except ValueError:
        print('Введите число от 1-5. Попробуйте еще раз')
