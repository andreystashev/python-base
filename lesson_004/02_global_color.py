# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


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
        v.draw(color=colors[value]['value'])
        point = v.end_point
        angle += angle_change


colors = {
    '1': {'title': 'red', 'value': sd.COLOR_RED},
    '2': {'title': 'orange', 'value': sd.COLOR_ORANGE},
    '3': {'title': 'yellow', 'value': sd.COLOR_YELLOW},
    '4': {'title': 'green', 'value': sd.COLOR_GREEN},
    '5': {'title': 'cyan', 'value': sd.COLOR_CYAN},
    '6': {'title': 'blue', 'value': sd.COLOR_BLUE},
    '7': {'title': 'purple', 'value': sd.COLOR_PURPLE}
}

for value, name in colors.items():
    print(value, name['title'])

while True:
    value = input("Введите желаемый цвет: ")
    color_input = (value)
    print('Вы ввели', value)

    if value in colors:

        point0 = sd.get_point(50, 50)
        draw_triangle(point=point0, angle=0, length=200)

        point0 = sd.get_point(50, 350)
        draw_square(point=point0, angle=0, length=200)

        point0 = sd.get_point(350, 50)
        draw_pentagon(point=point0, angle=0, length=150)

        point0 = sd.get_point(350, 350)
        draw_hexagon(point=point0, angle=0, length=100)
        break
    else:
        print('не верно')

sd.pause()
