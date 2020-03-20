# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


colors = {
    '1': {'title': 'triangle'},
    '2': {'title': 'square'},
    '3': {'title': 'pentagon'},
    '4': {'title': 'hexagon'}
}

for value, name in colors.items():
    print(value, name['title'])
while True:

    user_input = input("Введите желаемую фигуру: ")
    value = int(user_input)
    print('Вы ввели', value)
    side = value + 2
    point0 = sd.get_point(420, 180)
    if value > 4 or value < 1:
        print('неверный номер')
    else:
        def constructor(point, length, side, width):
            angle = 360 / side
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

        constructor(point=point0, length=200, side=side, width=4)
        break


sd.pause()
