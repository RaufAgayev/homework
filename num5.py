proceeds = int(input("Введите выручку компании: "))
cost = int(input("Введите издержку фирмы: "))
result = proceeds - cost

if proceeds > cost:
    print('У вас прибыль! :)')
    print(f'Ваша прибыль: {result}')
else:
    print('У вас издержка! :(')

number_of_employees = int(input('Введите численность соотрудников: '))

if proceeds > cost:
    profit = result / number_of_employees
    print(f'Прибыль на одного соотрудника: {profit}')