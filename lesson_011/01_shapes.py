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
def draw_triangle(point, angle, length):
    v = sd.get_vector(start_point=point)
    v.draw()
    point = v.end_point
    # point = point
    angle = angle
    length = length

def get_polygon(n):
    angle_change = 360 // n
    for v in range(0, 360, angle_change):
        draw_triangle()


    # TODO здесь ваш код


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
