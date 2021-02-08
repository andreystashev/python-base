# -*- coding: utf-8 -*-
from random import randint, choice


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

class SuicideError(Exception):
    pass


class DepressionError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DrunkError(Exception):
    pass


class IamGodError(Exception):
    pass


class CarCrashError(Exception):
    pass


error_list = [SuicideError, DepressionError, GluttonyError, DrunkError, IamGodError, CarCrashError]

ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    dice = randint(1, 13)
    if dice < 13:
        carma = randint(1, 7)
        return carma
    elif dice == 13:
        # Так получается, что выбросили одно, а сообщение уже будет от другого
        #  лучше так тогда
        today_error = choice(error_list)
        raise today_error(today_error.__name__)


while ENLIGHTENMENT_CARMA_LEVEL >= 0:
    try:
        ENLIGHTENMENT_CARMA_LEVEL -= one_day()
    except (SuicideError, DepressionError, GluttonyError, DrunkError, IamGodError, CarCrashError) as error:
        print(f'суть ошибки {error}')
print('карма накоплена')

# https://goo.gl/JnsDqu

# зачет!

