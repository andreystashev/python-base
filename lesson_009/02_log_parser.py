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


class Parser:
    interim_date_list = []
    date_dict = {}

    def __init__(self, file_name):
        self.file_name = file_name

    def time_cut(self):
        x = 11
        return x
        # pass

    def calculation(self):
        count = 0
        x = parser.time_cut()
        # todo получилось сделать корректное высчитывание, но моим способом не получается корректно высчитать год и месяц, потому
        #  что срез prev_date до и после циклов становится одинаковым, приходится брать информацию из файла
        prev_date = str(' 2018-05-14 19:38'[1:x])
        with open(self.file_name, mode='r') as file:
            for line in file:
                if 'NOK' in line:
                    if prev_date in line:
                        count += 1
                        if count == 4968:
                            self.interim_date_list.append((prev_date, count))
                    elif prev_date not in line:
                        self.interim_date_list.append((prev_date, count))
                        prev_date = str(line[1:x])
                        count = 1
                    for _ in self.interim_date_list:
                        self.date_dict.update(self.interim_date_list)
                        break

    def create_file(self, file_name):
        file_name = file_name
        for time, nok_number in self.date_dict.items():
            file = open(file_name, mode='a')
            file_content = ('[' + str(time) + '] ' + str(nok_number) + '\n')
            file.write(file_content)
            file.close()


class Hour(Parser):
    def time_cut(self):
        x = 17
        return x


parser = Parser(file_name='events.txt')
parser.calculation()
parser.create_file(file_name='events.nok.txt')
hr = Hour(Parser)
hr.time_cut()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# не пойму, почему не так считает, пробовал разные команды:

# z = dict.fromkeys([date],value)
# minute_d1.update(z)
# dd = collections.defaultdict(None,([date],value))
# print(dd)
# if date in minute_d1.keys():
#     value += 1
#     print('ge')
# #     # minute_d1.update(z)
# else:
#     minute_d1.update(date,value)
#     print(minute_d1)
# minute_d1.values(value)
# print(minute_d1)
#  я так понял, что правильным решением будет не создавать лишний словарь и список, а изначально один словарь
#  расширять потому что либо создается один словарь к каждой строке, либо туда за раз все ключи со значениями
#  добавляются и повторяющиеся исчезают, поэтому после этого не работает проверка на  наличие ключа
#  Здесь можно вообще без словаря обойтись, подскзал в самом классе


# Неверно статистику по минутам выводит. Можно увидеть из исхоного файла, что начитаться выходной файл должен так -
# [2018-05-14 19:38] 4
# [2018-05-14 19:39] 1
# [2018-05-14 19:40] 1
# [2018-05-14 19:42] 1
# [2018-05-14 19:43] 2
# [2018-05-14 19:44] 1
# [2018-05-14 19:45] 2
#  ...

#  по шаблонному методу в предыдущем задании написал, тоже не пойму как сделать
# И аналогично, применим Шаблонынй метод для получения аналогичного файла за час, месяц, год.
#  Здесь в наследниках нам достаточно будет только переопределять значение, до которого мы обрезаем строку -
#   для минут это было 17, для часов будет 14 и т.д.
# todo по наследникам в первом задании задал вопрос
