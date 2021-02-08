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
    angle_change = 360 // n

    def any_shape(point, length, zero_angle):
        start_point = point
        for angle in range(0, 360 - angle_change, angle_change):
            side = sd.get_vector(start_point=point, angle=angle+zero_angle, length=length)
            side.draw()
            point = side.end_point
        sd.line(start_point=start_point, end_point=point)

    return any_shape(point=sd.get_point(200, 200), length=200, zero_angle=0)


get_polygon(n=8)

sd.pause()

# зачет!
