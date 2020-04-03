# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_triangle(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3, side_change=3)


def draw_square(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3, side_change=4)


def draw_pentagon(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3, side_change=5)


def draw_hexagon(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3, side_change=6)


def any_shape(point, length, angle, width, side_change):
    angle_change = 360 // side_change
    for v in range(0, 360, angle_change):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v.draw()
        point = v.end_point
        angle += angle_change


shapes = {
    '1': {'title': 'triangle', 'function': draw_triangle},
    '2': {'title': 'square', 'function': draw_square},
    '3': {'title': 'pentagon', 'function': draw_pentagon},
    '4': {'title': 'hexagon', 'function': draw_hexagon}
}

for value, name, in shapes.items():
    print(value, name['title'])
point0 = sd.get_point(200, 200)

while True:

    value_input = input("Введите номер фигуры: ")
    shape_input = value_input
    print('Вы ввели', value_input)
    if value_input in shapes:
        shapes[value_input]['function'](point=point0, angle=0, length=200)
        break
    else:
        print('неверный номер')

sd.pause()
