# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
num = 0
while True:
    num += 1
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month = int(user_input)
    print('Вы ввели', month)

    monthes = [1, 3, 5, 7, 8, 10, 12]
    if month in monthes:
        print(31)
    elif month == 2:
        print(28)
    elif month > 12 or month < 1:
        print('так нельзя, досвидания')
        break
    elif num > 10:
        print('слишком много запросов, досвидания')
        break
    else:
        print(30)

# зачет!
