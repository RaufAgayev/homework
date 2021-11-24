first = int(input('Select the first number: '))
second = int(input('Select the second number: '))


def function(a, b):
    if b == 0:
        return 'Error'
    else:
        return f'Your answer is: {a / b}'


print(function(first, second))