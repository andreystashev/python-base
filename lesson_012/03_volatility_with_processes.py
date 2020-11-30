# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
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
from utilites import time_track, show_result, generate_filenames

import multiprocessing


class Ticker(multiprocessing.Process):

    def __init__(self, ticket_folder, collector=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticket_folder = ticket_folder
        self.name_ticket = ''
        self.volatility = 0
        self.collector = collector

    def run(self):
        # TODO этот метод у нас почти без изменений
        self.calculate(self.open())
        collector = multiprocessing.Queue()
        # self.collector.put(open())#

    def open(self):
        price_scope = []
        with open(self.ticket_folder, mode='r') as open_ticker:
            for element in open_ticker:
                scattered_element = element.split(',')
                self.name_ticket = scattered_element[0]
                if scattered_element[2] != 'PRICE':
                    price_scope.append(float(scattered_element[2]))
            return price_scope

    def calculate(self, unsorted):
        unsorted.sort()
        half_sum = (unsorted[0] + unsorted[-1]) / 2
        self.volatility = ((unsorted[-1] - unsorted[0]) / half_sum) * 100
        # TODO после того как получили валатильность вам нужно в трубу закинуть эти данные, чтобы из вне их отлавливать
        # TODO это можно делать тут. Метод пут нудно применять тут используя self.collector


@time_track
def main(folder):
    collector = multiprocessing.Queue()
    zero_tickers = []
    value_key = {}
    sorted_place = []
    tickers = []

    for last_folder in generate_filenames(folder):
        # TODO тут на вход нужно передавать collector еще
        tickers.append(Ticker(last_folder))

    # TODO тут лучше использовать бесконечный цикл, в нем конструкцию для отлавливания ошибки Empty
    # TODO в самом цикле нужно получать из очереди методом get значения которые там есть
    # TODO и обработку делать тоже в этом цикле, то что у вас написано с 86 строки до 91
    while not collector.empty():
        # TODO запуск нужно делать вне цикла, до него
        for ticker in tickers:
            ticker.start()
        # TODO эту часть нужно делать после цикла то же вне
        for ticker in tickers:
            ticker.join()




    for ran_ticker in tickers:
        if ran_ticker.volatility == 0:
            zero_tickers.append(ran_ticker.name_ticket)
        else:
            value_key[ran_ticker.volatility] = ran_ticker.name_ticket
            sorted_place.append(ran_ticker.volatility)
            sorted_place.sort()

    show_result(sorted_place, value_key, zero_tickers)


# Core 4 по 1.4Hz - Функция работала   секунд(ы)
# Core 4 по 2.4Hz - Функция работала   секунд(ы)
path = "trades/"
if __name__ == '__main__':
    main(folder=path)
