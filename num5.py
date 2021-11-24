string_counts = (input('Введите числа: ')).split(' ')

new_list = []


for i in range(0, len(string_counts)):
    new_list.append(int(string_counts[i]))

sum_counts = sum(new_list)
print(sum_counts)

continue_program = input('Нажмите "Enter" чтобы продолжить')

while continue_program == '':
    string_counts = (input('Введите числа: ')).split(' ')
    for i in range(0, len(string_counts)):
        if string_counts[i].isdigit():
            new_list.append(int(string_counts[i]))
        else:
            continue_program = 'Error'
            print('Program was finish')
    print(sum(new_list))