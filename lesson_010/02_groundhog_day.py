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
exception_list = ['SuicideError', 'DepressionError', 'GluttonyError', 'CarCrashError', 'DrunkError', 'IamGodError']

ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    dice = randint(1, 13)
    if dice < 13:
        global carma
        carma = randint(1, 7)
    elif dice == 13:
        error = exception_list[randint(0, 5)]
        raise BaseException(error)


while ENLIGHTENMENT_CARMA_LEVEL >= 0:
    try:
        one_day()
    except BaseException as first_error:
        print(f'Суть ошибки: {first_error}')
    ENLIGHTENMENT_CARMA_LEVEL = ENLIGHTENMENT_CARMA_LEVEL - carma
    if ENLIGHTENMENT_CARMA_LEVEL <= 0:
        print('карма накоплена')

# https://goo.gl/JnsDqu
