# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.



# for _ in range(10):
#     #
#     point = sd.random_number(-270, 270)
#     point4 = sd.random_number(-270, 270)
#     x = 300 + point
#     y = 300 + point4
#     left_bottom = sd.get_point(x=x - 25, y=y - 25)
#     right_top = sd.get_point(x=x + 25, y=y - 1)
#     left_bottom1 = sd.get_point(x=x - 21, y=y - 21)
#     right_top1 = sd.get_point(x=x + 21, y=y - 5)
#     point0 = sd.get_point(x, y)
#     point1 = sd.get_point(x=x + 20, y=y + 20)
#     point2 = sd.get_point(x=x - 20, y=y + 20)
#     radius = 50
#     radius1 = 10
#     sd.circle(center_position=point0, radius=radius, width=3)
#     sd.circle(center_position=point1, radius=radius1, color=sd.COLOR_WHITE, width=6)
#     sd.circle(center_position=point2, radius=radius1, color=sd.COLOR_WHITE, width=6)
#     sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=5)
#     sd.rectangle(left_bottom=left_bottom1, right_top=right_top1, color=sd.COLOR_WHITE, width=0)


# TODO Вот значения x и y нужно передавать в функцию. То есть мы можем передать конкретные координаты,
#  которые будут центром нашего смайлика
def smile(point, color):
    radius = 50
    # TODO Тут бы лучше более говорящий нейминг сделать - цвет_рта, цвет_глаз
    color1 = sd.COLOR_WHITE
    color2 = sd.COLOR_RED
    sd.circle(center_position=sd.get_point(x, y), color=color, radius=radius, width=49)
    sd.circle(center_position=sd.get_point(x + 20, y + 20), color=color1, radius=radius - 37, width=8)
    sd.circle(center_position=sd.get_point(x - 20, y + 20), color=color1, radius=radius - 37, width=8)
    sd.rectangle(left_bottom=sd.get_point(x=x - 25, y=y - 25), right_top=sd.get_point(x=x + 25, y=y - 1), width=5)
    sd.rectangle(left_bottom=sd.get_point(x=x - 21, y=y - 21), color=color2, right_top=sd.get_point(x=x + 21, y=y - 5),
                 width=0)


for _ in range(10):
    # TODO А здесь получаем рандомную точку, можно через sd.random_point(), и передаем в функцию
    #  x и y этой точки. Или просто два рандомных числа в качестве координат передаем.
    point = sd.random_number(-270, 270)
    point1 = sd.random_number(-270, 270)
    x = 300 + point
    y = 300 + point1
    color = sd.random_color()  # TODO И рандомный цвет, это правильно сделано

    smile(point=point, color=color)

sd.pause()

# TODO Так у нас есть шаблон рисования смайлика и можем импортировать функцию в другой модуль и
#  нарисовать смайлик в любых конкретных координатах и любым нужным нам цветом.
#  В 5 модуле это нам понадобится.
