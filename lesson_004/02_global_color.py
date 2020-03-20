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

# TODO Аналогично, определения функций убираем наверх

# TODO Сделаем сразу словарь такого вида
#  colors = {
#      '1': {'title': 'red', 'value': sd.COLOR_RED},
#      '2': {'title': 'orange', 'value': sd.COLOR_ORANGE},
#      ...
#  }

# TODO Тут сделать распечатку номер - название цвета в цикле через colors.items()
print('Возможные цвета: \n 1 : red \n 2 : orange \n 3 : yellow \n 4 : green \n 5 : cyan \n 6 : blue \n 7 : purple')

while True:
    user_input = input("Введите желаемый цвет: ")
    color_input = int(user_input)
    print('Вы ввели', color_input)
    # TODO И здесь сразу получаем цвет из словаря и делаем вызов функций
    #  Таким образом у нас код станет более поддерживаемым -
    #  если нам надо будет добавить еще цвет, мы добавим только 1 строчку в словарь
    colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
              sd.COLOR_PURPLE]
    if color_input == 1:
        color = colors[0]
    elif color_input == 2:
        color = colors[1]
    elif color_input == 3:
        color = colors[2]
    elif color_input == 4:
        color = colors[3]
    elif color_input == 5:
        color = colors[4]
    elif color_input == 6:
        color = colors[5]
    elif color_input == 7:
        color = colors[6]
    else:
        # TODO Если номер неверный, то нужно опять запросить ввод. То есть пока юзер не введет верный цвет,
        #   цикл останавливать не нужно
        print('вы ввели некорректный номер')
        break

    # TODO Цвет нужно передавать в функцию как входной параметр. Сейчас он берется из глобальной области видимости,
    #   что не есть хорошо
    def triangle(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
        v2.draw(color=color)

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
        v3.draw(color=color)


    point0 = sd.get_point(20, 20)
    triangle(point=point0, angle=0, length=200)


    def square(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
        v2.draw(color=color)

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
        v3.draw(color=color)

        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
        v4.draw(color=color)


    point0 = sd.get_point(300, 20)
    square(point=point0, angle=0, length=200)


    def pentagon(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
        v2.draw(color=color)

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
        v3.draw(color=color)

        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
        v4.draw(color=color)

        v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
        v5.draw(color=color)


    point0 = sd.get_point(50, 350)
    pentagon(point=point0, angle=0, length=100)


    def hexagon(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
        v2.draw(color=color)

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
        v3.draw(color=color)

        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
        v4.draw(color=color)

        v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
        v5.draw(color=color)

        v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
        v6.draw(color=color)


    point0 = sd.get_point(350, 350)
    hexagon(point=point0, angle=0, length=100)
    break

sd.pause()
