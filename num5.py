my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новое число рейтинга: '))
list_index = 0

for i in my_list:
    if new_element <= i:
        list_index += 1
    elif new_element > i:
        my_list.insert(i, new_element)
        break

my_list.pop()
my_list.insert(list_index, float(new_element))
print(my_list)