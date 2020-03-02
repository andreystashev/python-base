# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)




# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600, 500)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)






# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет


# TODO Функция должна принимать цвет рисования в качестве входного параметра
def bubble(point, step):
    radius = 50
    COLOR_WHITE = (255, 255, 255)
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=COLOR_WHITE, width=2)


point = sd.get_point(100, 500)
bubble(point=point, step=10)




# Нарисовать 10 пузырьков в ряд


for x in range (100,1100,100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)




# Нарисовать три ряда по 10 пузырьков

for y in range (100,330,100):
    for x in range (100,1100,100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)




# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range (100):
    point = sd.random_point()
    # TODO И тут нужно нарисовать пузырьки рандомными цветами
    bubble(point=point, step=5)








sd.pause()


# TODO Везде нужно обращать внимание, что PyCharm подчеркивает зеленой линией - чаще всего это недочеты по PEP 8.
#  (PEP8 - это рекомендации по стилю написания кода - см https://pep8.ru/doc/pep8/)
#  Все эти недочеты тоже необходимо устранить.
#  Чтобы не делать все вручную, можно использовать меню PyCharm: Code / Reformat Code






