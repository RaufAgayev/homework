time = int(input('Введите время в секундах: '))
seconds = time % 60
minutes = (time // 60) % 60
hours = time // 60 // 60

if seconds < 10:
    seconds = '0' + str(time % 60)
if minutes < 10:
    minutes = '0' + str((time // 60) % 60)
if hours < 10:
    hours = '0' + str(time // 60 // 60)
print(f'Ваше время {hours}:{minutes}:{seconds}')