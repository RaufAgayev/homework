# 1-ое решение
x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))


def my_func(x, y):
    result = f'Ваш ответ: {x ** y}'
    return result


print(my_func(x, y))

# 2-ое решение

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

my_list = []
y = abs(y)


def my_func(x, y):
    main = x
    for i in range(0, y):
        my_list.append(x)

    for i in range(1, y):
        main = main * x
    result = 1 / main
    return f'Ваш ответ: {result}'


print(my_func(x, y))