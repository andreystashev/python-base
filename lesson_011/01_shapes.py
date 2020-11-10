# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


# TODO давайте доработаем функцию видно что на 8 угольнике крайний вектор не доходит,
# TODO чтобы это исправить нужно использовать sd.line() после цикла for
def get_polygon(n):
    def any_shape(point, length, angle):
        # TODO эту переменную вынести в функцию get_polygon в ее область видимости!
        angle_change = 360 // n
        # TODO что есть переменная v и где она используется ? Угол наклона вектора получать тут
        # TODO Что бы не "крутить" крайний вектор нужно в рендж сделать так (0, 360-angle_change, angle_change):
        for v in range(0, 360, angle_change):
            v = sd.get_vector(start_point=point, angle=angle, length=length)
            v.draw()
            point = v.end_point
            # TODO Угол наклона вектора получать в цикле!
            angle += angle_change
        # TODO тут рисовать линию от начало до point, начальную точку нужно сохранить изначально!

    return any_shape(point=sd.get_point(200, 200), length=200, angle=0)


get_polygon(n=8)

sd.pause()
