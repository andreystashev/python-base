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



def constructor(point, length, side, width):
    angle = 360 / side
    # TODO А почему бы просто в цикле for по side не нарисовать вектор?
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle * 2, length=length, width=width)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle * 3, length=length, width=width)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle * 4, length=length, width=width)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle * 5 + 1, length=length, width=width)
    if side == 5:
        v5.draw()
    if side == 6:
        v5.draw()
        sd.line(start_point=v5.end_point, end_point=point0, width=width)

# TODO И не совсем верно.
#  По заданию подразумевается, что мы для каждой фигуры сделаем свою функцию, но на основе общей функции, то есть -
#  def draw_triangle(point, angle, length):
#      any_shape(point=point, angle=angle, length=length, sides=3)

# TODO И с остальными аналогично

# TODO Просто если мы в коде встретим запись типа constructor(), то непонятно, что это за фигура, надо лезть
#   в ее исходники, тратит время. А если draw_triangle - то тут как-бы все понятно.

point0 = sd.get_point(220, 20)
constructor(point=point0, length=200, side=3, width=4)
point0 = sd.get_point(580, 20)
constructor(point=point0, length=200, side=4, width=4)
point0 = sd.get_point(270, 250)
constructor(point=point0, length=200, side=5, width=4)
point0 = sd.get_point(530, 350)
constructor(point=point0, length=100, side=6, width=4)


sd.pause()
