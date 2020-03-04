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


def smile(x, y, color):
    radius = 50
    eye_color = sd.COLOR_WHITE
    throat_color = sd.COLOR_RED
    sd.circle(center_position=sd.get_point(x, y), color=color, radius=radius, width=49)
    sd.circle(center_position=sd.get_point(x + 20, y + 20), color=eye_color, radius=radius - 37, width=8)
    sd.circle(center_position=sd.get_point(x - 20, y + 20), color=eye_color, radius=radius - 37, width=8)
    sd.rectangle(left_bottom=sd.get_point(x=x - 25, y=y - 25), right_top=sd.get_point(x=x + 25, y=y - 1), width=5)
    sd.rectangle(left_bottom=sd.get_point(x=x - 21, y=y - 21), color=throat_color,
                 right_top=sd.get_point(x=x + 21, y=y - 5),
                 width=0)


for _ in range(10):
    random_point = sd.random_point()
    random_color = sd.random_color()
    smile(x=random_point.x, y=random_point.y, color=random_color)

sd.pause()
