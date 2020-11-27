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

from utilites import time_track, generate_filenames, show_result


class Ticker:

    # TODO класс должен принимать только путь до файла
    def __init__(self, ticket_folder, name_ticket):
        self.ticket_folder = ticket_folder
        # TODO название можно получить в методе open
        self.name_ticket = name_ticket
        # TODO где то в коде мы должны получать этот параметр
        self.volatility = 0

    # TODO Метод run ничего возвращать не должен.
    def run(self):
        # TODO для чего мы три раза вызываем метод open и два раза метод calculate?
        self.open()
        name = self.calculate(self.open())[1][7:11]
        volatility = self.calculate(self.open())[0]

        return name, volatility

    def open(self):
        # TODO нейминг переменной
        price_list = []
        # TODO для открытия файла используем контекстный менеджер
        open_ticker = open(self.ticket_folder + self.name_ticket, mode='r')
        for element in open_ticker:
            # TODO результат этой строки наверно нужно записать в переменную чтобы потом еще раз не сплитить
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
    # TODO дублирование переменной
    ticket_folder = ticket_folder
    zero_tickers = []
    object_scope = []
    key_value = {}
    value_key = {}
    sorted_place = []
    # TODO как воспользоваться генератором который возвращает каждый раз путь до файла:
    # TODO цикл путь_до_файла итерируемся по generate_filenames(ticket_folder)
    # TODO в цикле мы наполним список(можно назвать так tickers) экземплярами класса Ticker(путь_до_файла)

    # TODO object зарезервированое слово системой использовать не рекомендуется
    for object in generate_filenames(ticket_folder, Ticker):
        object_scope.append(object)
    for value in object_scope:
        key_value[value.run()[0]] = value.run()[1]

    sorted_scope = list(key_value.items())
    sorted_scope.sort(key=lambda part: part[1])
    for part in sorted_scope:
        if part[1] == 0:
            zero_tickers.append(part[0])
        else:
            value_key[part[1]] = part[0]
            sorted_place.append(part[1])
            sorted_place.sort()
    show_result(sorted_place, value_key, zero_tickers)


folder = "trades/"
if __name__ == '__main__':
    main(ticket_folder=folder)

# TODO код отработал очень долго - Функция работала 25.4708 секунд(ы)
# TODO Нужно оптимизировать
