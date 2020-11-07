# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def grouped_events():
    prev_time = None
    nok_counter = 0
    with open('events.txt', mode='r') as file:
        for line in file:
            if 'NOK' in line:
                time = line[1:17]
                if time != prev_time:
                    if prev_time is not None:
                        yield prev_time, nok_counter
                    prev_time = time
                    nok_counter = 0
                nok_counter += 1
    if nok_counter > 0:
        yield prev_time, nok_counter


for group_time, event_count in grouped_events():
    print(f'[{group_time}] {event_count}')
