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
        pass

    def calculation(self):
        count = 0
        x = self.time_cut()
        with open(self.file_name, mode='r') as file:
            prev_date = (next(file)[1:x])  # TODO: в этом случае, если в строчке есть NOK, то он не учтется
            for line in file:
                if 'NOK' in line:
                    if prev_date in line:
                        count += 1
                        self.interim_date_list.append((prev_date, count))
                        self.date_dict.update(self.interim_date_list)
                    else:
                        self.interim_date_list.append((prev_date, count))
                        prev_date = str(line[1:x])
                        count = 1
                        self.date_dict.update(self.interim_date_list)

    def create_file(self, file_name):
        file_name = file_name
        file = open(file_name, mode='a')
        for time, nok_number in self.date_dict.items():
            if nok_number > 0:
                file_content = ('[{}] {}\n'.format(str(time), str(nok_number)))
                file.write(file_content)
        file.close()


class Year(Parser):
    def time_cut(self):
        x = 5
        return x


class Month(Parser):
    def time_cut(self):
        x = 8
        return x


class Hour(Parser):
    def time_cut(self):
        x = 14
        return x


class Minute(Parser):
    def time_cut(self):
        x = 17
        return x


minute = Minute(file_name='events.txt')
minute.calculation()
minute.create_file(file_name='events.nok.txt')

# hour = Hour(file_name='events.txt')
# hour.calculation()
# hour.create_file(file_name='events.nok.txt')

# month = Month(file_name='events.txt')
# month.calculation()
# month.create_file(file_name='events.nok.txt')

# year = Year(file_name='events.txt')
# year.calculation()
# year.create_file(file_name='events.nok.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
