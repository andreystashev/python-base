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
        angle_change = 360 // n
        for v in range(0, 360, angle_change):
            v = sd.get_vector(start_point=point, angle=angle, length=length)
            v.draw()
            point = v.end_point
            angle += angle_change

    return any_shape(point=sd.get_point(200, 200), length=200, angle=0)


get_polygon(n=3)

sd.pause()
