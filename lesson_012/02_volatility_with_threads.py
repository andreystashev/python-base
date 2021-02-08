# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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

import threading


class Ticker(threading.Thread):

    def __init__(self, ticket_folder, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticket_folder = ticket_folder
        self.name_ticket = ''
        self.volatility = 0

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


@time_track
def main(folder):
    zero_tickers = []
    value_key = {}
    sorted_place = []
    tickers = []

    for last_folder in generate_filenames(folder):
        tickers.append(Ticker(last_folder))

    for ticker in tickers:
        ticker.start()
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


# Core 4 по 1.4Hz - Функция работала 2.3727 секунд(ы)
# Core 4 по 2.4Hz - Функция работала 4.2292 секунд(ы)
path = "trades/"
if __name__ == '__main__':
    main(folder=path)

# зачет!
