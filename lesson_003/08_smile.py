# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# Git все помнит, нет необходимости оставлять закомментированный код

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

# зачет!
