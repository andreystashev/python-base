# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO Аналогично, делаем через классы и работаем с неймингом

file_name = 'events.txt'

minute_d = []
minute_d1 = {}
minute_d2 = {}

with open(file_name, mode='r') as file:
    for line in file:
        for line in file:
            linelist = line.split()
            if 'NOK' in linelist[2]:
                value = 0
                date = str(line[1:17])
                minute_d1 = {date: value}
            if date in minute_d1.keys():
                value += 1
                date = line[1:17]
                minute_d.append((date, value))
                for i in minute_d:
                    minute_d2.update(minute_d)

                    break
for key, value in minute_d2.items():
    # print(int(key[11:16]))
    int_b = int(key[11:16].replace(':', ''))
    # print("The integer value", int_b)  Не пойму, каким образом отсортировать числа. Из мыслей - преобразоват
    #                                       строку в число, добавить в список и сделать сортировку, но тогда вопрос - как
    #                                       связать получившиеся числа с изначальными ключами ввиде строк и значениями
    # TODO А зачем их сортировать? Записываем в файл, как есть


for key, value in minute_d2.items():
    file_name = 'events.nok.txt'
    file = open(file_name, mode='a')
    file_content = ('[' + str(key) + '] ' + str(value) + '\n')
    file.write(file_content)
    file.close()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
