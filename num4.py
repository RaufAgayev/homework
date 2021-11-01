words = input('Напишите слова через пробелы: ')
list_words = words.split()
for i, word in enumerate(list_words, 1):
    print(f'{i} {word[:10]}')
