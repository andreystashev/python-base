# -*- coding: utf-8 -*-
import os
import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


def show_result(sort_folder, final_folder, zero_folder):
    sort_folder = sort_folder
    final_folder = final_folder
    zero_folder = zero_folder
    zero_folder.sort()
    sort_folder.reverse()

    print('нулевая волатильность: ', '\n', ', '.join(zero_folder))
    print('минимальная волатильность: ')
    for min_ticker in sort_folder[-3:]:
        print(final_folder[min_ticker], round(min_ticker, 2), '%')
    print('максимальная волатильность: ')
    for max_ticker in sort_folder[:3]:
        print(final_folder[max_ticker], round(max_ticker, 2), '%')


def generate_filenames(folder):
    for dir_path, dir_names, file_names in os.walk(folder):
        for file_name in file_names:
            yield folder + file_name
