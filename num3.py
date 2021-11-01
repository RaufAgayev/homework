while True:
    month = input('Введите номер месяца от 1 до 12: ')
    if month.isdigit() and 0 < int(month) > 12:
        first_season = ["зима", "весна", "лето", "осень"]
        second_season = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
        print(f'Список сезонов {first_season[int(month) // 3]}')
        print(f'Словарь сезонов {second_season[int(month) // 3]}')
        break
    else:
        print("Не правильный ввод данных")
        