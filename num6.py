first_day = int(input("Введите число в км: "))
min_km = int(input("Введите число в км: "))
day = 1
print(first_day)

while True:
    first_day = first_day + (first_day * 10 / 100)
    print(first_day)
    if first_day < min_km:
        day += 1
    else:
        print('на ' + str(day + 1) + ' день спортсмен достиг результата — не менее ' + str(min_km) + ' км.')
        break
