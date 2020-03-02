# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO Всю отрисовку смайлика нужно сложить в отдельную функцию.
#  То есть внутри функции рисуется только один смайлик.

for _ in range (10):
    # TODO А потом вызываем нашу функцию smile 10 раз в цикле в рандомных точках и рандомным цветом
    point = sd.random_number(-270,270)
    point4 = sd.random_number(-270,270)
    x=300+point
    y=300+point4
    left_bottom = sd.get_point(x=x-25,  y=y-25)
    right_top = sd.get_point(x=x+25,y=y-1)
    left_bottom1 = sd.get_point(x=x-21,  y=y-21)
    right_top1 = sd.get_point(x=x+21,y=y-5)
    point0 = sd.get_point(x, y)
    point1 = sd.get_point(x=x+20,y=y+20)
    point2 = sd.get_point(x=x-20,y=y+20)
    radius = 50
    radius1 = 10
    sd.circle(center_position=point0, radius=radius, width=3)
    sd.circle(center_position=point1, radius=radius1, color=sd.COLOR_WHITE,width=6)
    sd.circle(center_position=point2, radius=radius1, color=sd.COLOR_WHITE,width=6)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=5)
    sd.rectangle(left_bottom=left_bottom1, right_top=right_top1, color=sd.COLOR_WHITE, width=0)





sd.pause()

# TODO И PEP 8
