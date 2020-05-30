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

    def calculation(self):
        with open(self.file_name, mode='r') as file:
            for _ in file:
                for line in file:
                    fragment_line_list = line.split()
                    if 'NOK' in fragment_line_list[2]:
                        nok_counter = 0
                        date = str(line[1:17])
                        interim_date_dict = {date: nok_counter}
                    if date in interim_date_dict.keys():
                        nok_counter += 1
                        date = line[1:17]
                        self.interim_date_list.append((date, nok_counter))

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


parser = Parser(file_name='events.txt')
parser.calculation()
parser.create_file(file_name='events.nok.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# TODO не пойму, почему не так считает, пробовал разные команды:

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
# TODO я так понял, что правильным решением будет не создавать лишний словарь и список, а изначально один словарь
#  расширять потому что либо создается один словарь к каждой строке, либо туда за раз все ключи со значениями
#  добавляются и повторяющиеся исчезают, поэтому после этого не работает проверка на  наличие ключа


# Неверно статистику по минутам выводит. Можно увидеть из исхоного файла, что начитаться выходной файл должен так -
# [2018-05-14 19:38] 4
# [2018-05-14 19:39] 1
# [2018-05-14 19:40] 1
# [2018-05-14 19:42] 1
# [2018-05-14 19:43] 2
# [2018-05-14 19:44] 1
# [2018-05-14 19:45] 2
#  ...

# TODO по шаблонному методу в предыдущем задании написал, тоже не пойму как сделать
# И аналогично, применим Шаблонынй метод для получения аналогичного файла за час, месяц, год.
