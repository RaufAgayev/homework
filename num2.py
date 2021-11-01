elements = input('Введите элементы массива разделяя их пробелами: ').split()
i = 0
print(f'Оригинальный список {elements}')
while i + 1 < len(elements):                    # i + 1 для того чтобы избежать ошибки out of range
    if i % 2 == 0:
        elements.insert(i, elements.pop(i + 1))
    i += 1
print(f'Изменёный список {elements}')