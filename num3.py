n = input('Введите число: ')

first_n = int(n)
second_n = int(str(n) + str(n))
third_n = int(str(n) + str(n) + str(n))
result = first_n + second_n + third_n

print(f'Сумма чисел = {first_n} + {second_n} + {third_n} = {result}')