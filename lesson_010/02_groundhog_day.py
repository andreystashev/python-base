# -*- coding: utf-8 -*-
from random import randint


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


ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    dice = randint(1, 13)
    if dice < 13:
        carma = randint(1, 7)
    elif dice == 13:
        raise Exception
    return carma


while ENLIGHTENMENT_CARMA_LEVEL >= 0:
    try:
        one_day()
    except Exception as error:
        print(f'Суть ошибки: {error}')
    ENLIGHTENMENT_CARMA_LEVEL = ENLIGHTENMENT_CARMA_LEVEL - carma
    print('карма накоплена')

# https://goo.gl/JnsDqu
