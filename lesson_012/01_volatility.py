# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import os

from lesson_012.python_snippets.utils import time_track


class Ticker:

    def __init__(self, ticket_folder, name_ticket):
        self.ticket_folder = ticket_folder
        self.name_ticket = name_ticket
        self.volatility = 0

    def run(self):
        self.open()
        name = self.calculate(self.open())[1][7:11]
        volatility = self.calculate(self.open())[0]

        return name, volatility

    def open(self):
        price_list = []
        open_ticker = open(self.ticket_folder + self.name_ticket, mode='r')
        for element in open_ticker:
            element.split(',')
            if element.split(',')[2] != 'PRICE':
                price_list.append(float(element.split(',')[2]))
        return price_list, self.name_ticket

    def calculate(self, unsorted):
        sorted_elements = unsorted[0]
        sorted_elements.sort()
        half_sum = (sorted_elements[0] + sorted_elements[-1]) / 2
        volatility = ((sorted_elements[-1] - sorted_elements[0]) / half_sum) * 100
        return volatility, unsorted[1]


@time_track
def main(ticket_folder):
    zero_list = []
    list_sort = []
    tickers_dict = {}
    ticket_folder = ticket_folder
    for dirpath, dirnames, filenames in os.walk(ticket_folder):

        for ticket_files in filenames:
            ticker = Ticker(ticket_folder=ticket_folder, name_ticket=ticket_files)
            name = ticker.run()[0]
            value = ticker.run()[1]
            tickers_dict[value] = name
            if value == 0:
                zero_list.append(name)
            else:
                list_sort.append(value)
                list_sort.sort()

        for min in list_sort[0:3]:
            print(min, tickers_dict[min], '- минимальная волатильность')
        for max in list_sort[-3:]:
            print(max, tickers_dict[max], '- максимальная волатильность')
        print('нулевая волатильность: ', zero_list)


folder = "/Users/andrey/PycharmProjects/python_base/lesson_012/trades/"
if __name__ == '__main__':
    main(ticket_folder=folder)
