def int_func(word):
    result = word.title()
    return result


text = 'text'

print(int_func(text))


def function(string):
    split_list = string.split()
    split_list.append(int_func(text))
    str_words = ' '.join(split_list)
    answer = str_words.title()
    return answer


print(function(input('Ведите слова латинскими буквами: ')))
