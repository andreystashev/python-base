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

def get_polygon(n):
    def any_shape(point, length, angle):
        startpoint = point
        # TODO нижнюю строчку нужно переместить в цикл фор?
        angle_change = 360 // n
        #  что есть переменная v и где она используется ? Угол наклона вектора получать тут
        for _ in range(0, 360 - angle_change, angle_change):
            side = sd.get_vector(start_point=point, angle=angle, length=length)
            side.draw()
            point = side.end_point
            # Угол наклона вектора получать в цикле!
            # TODO нижнюю строчку нужно переместить отсюда? Если производить какие-то манипуляции со строчкаим, которые
            #  тудушками отмечены, то тогда код ломается
            angle += angle_change
        sd.line(start_point=startpoint, end_point=side.end_point)

    return any_shape(point=sd.get_point(200, 200), length=200, angle=0)


get_polygon(n=8)

sd.pause()
