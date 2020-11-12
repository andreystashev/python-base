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

    # TODO тут назовите angle -> zero_angel
    def any_shape(point, length, angle):
        # TODO нейминг переменной
        startpoint = point
        # TODO в цикле мы будем получать angle
        for _ in range(0, 360 - angle_change, angle_change):
            # TODO в sd.get_vector в параметре angle напишите сразу angle=angle+zero_angel
            side = sd.get_vector(start_point=point, angle=angle, length=length)
            side.draw()
            point = side.end_point
            # TODO Это строка нам не нужна если мы будем получать angle в цикле
            angle += angle_change
        # TODO используйте переменные start_point и point
        sd.line(start_point=startpoint, end_point=side.end_point)

    return any_shape(point=sd.get_point(200, 200), length=200, angle=0)


get_polygon(n=8)

sd.pause()
