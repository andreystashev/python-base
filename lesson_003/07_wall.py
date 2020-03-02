# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


# TODO По заданию у кирпича размеры 100х50
for z in range(-50,1100,150):
    z +=50
    left_bottom = sd.get_point(0+z,0)
    right_top = sd.get_point(150+z, 50)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)
    for q in range(0,1100,100):
        q +=50
        left_bottom = sd.get_point(100+z,0+q)
        right_top = sd.get_point(250+z, 50+q)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)
    for w in range(0,1100,100):
        w += 100
        left_bottom = sd.get_point(0 + z, 0 + w)
        right_top = sd.get_point(150 + z, 50 + w)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)

# TODO Можно упростить алгорим по такой логике -
#  для каждого У в диапазоне с ... по ... с шагом ....
#      для каждого Х в диапазоне с ... по ... с шагом ....
#          если строка четная:
#              сдвигаем x на 50
#          вычислиям левый нижний угол
#          вычисляем правый верхний угол
#          рисуем прямоугольник


# TODO И PEP 8












sd.pause()