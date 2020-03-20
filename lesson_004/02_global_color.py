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

point0 = sd.get_point(220, 20)
point1 = sd.get_point(580, 20)
point2 = sd.get_point(270, 250)
point3 = sd.get_point(530, 350)

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
    color_input = int(value)
    print('Вы ввели', value)

    if color_input > 4 or color_input < 1:
        print('неверный номер')
    else:
        def constructor(point, length, side, width):
            angle = 360 / side
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
            v1.draw(color=color)
            v2 = sd.get_vector(start_point=v1.end_point, angle=angle * 2, length=length, width=width)
            v2.draw(color=color)
            v3 = sd.get_vector(start_point=v2.end_point, angle=angle * 3, length=length, width=width)
            v3.draw(color=color)
            v4 = sd.get_vector(start_point=v3.end_point, angle=angle * 4, length=length, width=width)
            v4.draw(color=color)
            v5 = sd.get_vector(start_point=v4.end_point, angle=angle * 5 + 1, length=length, width=width)
            if side == 5:
                v5.draw(color=color)
            if side == 6:
                v5.draw(color=color)
                sd.line(start_point=v5.end_point, end_point=point3, width=width, color=color)


        if color_input == 1:
            color = colors[value]['value']
        elif color_input == 2:
            color = colors[value]['value']
        elif color_input == 3:
            color = colors[value]['value']
        elif color_input == 4:
            color = colors[value]['value']
        elif color_input == 5:
            color = colors[value]['value']
        elif color_input == 6:
            color = colors[value]['value']
        elif color_input == 7:
            color = colors[value]['value']

        constructor(point=point0, length=200, side=3, width=4)
        constructor(point=point1, length=200, side=4, width=4)
        constructor(point=point2, length=200, side=5, width=4)
        constructor(point=point3, length=100, side=6, width=4)

        break
# TODO Чтобы не прерывать цикл при неверном вводе пришлось запихнуть всё внутрь цикла,
#  также не понял про цвет из глобальной области видимости. Получается такой код - v1.draw(color=color) не правильный?
#   по другому если допустим в sd.get_vector добавлять цвет то выскакивает ошибка а если в def constructor,
#  то не срабатывает


sd.pause()
