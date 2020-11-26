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
    print('нулевая волатильность: ', zero_folder)
    for min in sort_folder[0:3]:
        print(min, final_folder[min], '- минимальная волатильность')
    for max in sort_folder[-3:]:
        print(max, final_folder[max], '- максимальная волатильность')


def generate_filenames(ticket_folder, class_name):
    for dir_path, dir_names, file_names in os.walk(ticket_folder):
        for file_name in file_names:
            ticker = class_name(ticket_folder=ticket_folder, name_ticket=file_name)
            yield ticker
