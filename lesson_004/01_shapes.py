# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

#
# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw()
#
#
# def square(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
#     v4.draw()
#
#
# def pentagon(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
#     v5.draw()
#
#
# def hexagon(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
#     v6.draw()
#
#
# point0 = sd.get_point(20, 20)
# triangle(point=point0, angle=0, length=200)
#
#
# point0 = sd.get_point(300, 20)
# square(point=point0, angle=0, length=200)
#
#
# point0 = sd.get_point(50, 350)
# pentagon(point=point0, angle=0, length=100)
#
#
# point0 = sd.get_point(350, 350)
# hexagon(point=point0, angle=0, length=100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def draw_triangle(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3)


def draw_square(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3)


def draw_pentagon(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3)


def draw_hexagon(point, angle, length):
    any_shape(point=point, angle=angle, length=length, width=3)


def any_shape(point, length, angle, width):
    for v in range(0, 360, angle_change):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v.draw()
        point = v.end_point
        angle += angle_change


point0 = sd.get_point(50, 50)
angle_change = 120
draw_triangle(point=point0, angle=0, length=200)

point0 = sd.get_point(50, 350)
angle_change = 90
draw_square(point=point0, angle=0, length=200)

point0 = sd.get_point(350, 50)
angle_change = 72
draw_pentagon(point=point0, angle=0, length=150)

point0 = sd.get_point(350, 350)
angle_change = 60
draw_hexagon(point=point0, angle=0, length=100)

sd.pause()

# todo не понял как реализовать изменение угла в функции. Пытался у каждой функции дополнительно указать колличество сторон
#  и сделать например через "if sides = 3 >> angle_change = 120" но это не работает, или работает но применяется ко всем
#  фигурам подряд
