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
from queue import Empty


class Ticker(multiprocessing.Process):

    def __init__(self, ticket_folder, collector=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticket_folder = ticket_folder
        self.name_ticket = ''
        self.volatility = 0
        self.collector = collector
        self.for_get = {}

    def run(self):
        self.calculate(self.open())

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
        self.for_get = {'name_ticket': self.name_ticket, 'volatility': self.volatility}
        return self.collector.put(self.for_get)


@time_track
def main(folder):
    zero_tickers = []
    value_key = {}
    sorted_place = []
    tickers = []
    collector = multiprocessing.Queue()

    for last_folder in generate_filenames(folder):
        tickers.append(Ticker(last_folder, collector=collector))
    for ticker in tickers:
        ticker.start()

    while True:
        try:
            collect = collector.get(True, 1)
            if collect['volatility'] == 0:
                zero_tickers.append(collect['name_ticket'])
            else:
                value_key[collect['volatility']] = collect['name_ticket']
                sorted_place.append(collect['volatility'])
                sorted_place.sort()
        except Empty:
            if not any(ticker.is_alive() for ticker in tickers):
                break

    for ticker in tickers:
        ticker.join()
    show_result(sorted_place, value_key, zero_tickers)


# Core 4 по 1.4Hz - Функция работала 2.0923 секунд(ы)
# Core 4 по 2.4Hz - Функция работала 2.7704 секунд(ы)
path = "trades/"
if __name__ == '__main__':
    main(folder=path)

