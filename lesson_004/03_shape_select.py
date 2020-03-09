# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

print('Возможные фигуры: \n 1 : треугольник \n 2 : квадрат \n 3 : пятиугольник \n 4 : шестиугольник')

user_input = input("Введите желаемую фигуру: ")
f_input = int(user_input)
print('Вы ввели', f_input)
if f_input == 1:
    def triangle(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
        v2.draw()

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
        v3.draw()


    point0 = sd.get_point(200, 200)
    triangle(point=point0, angle=0, length=200)

elif f_input == 2:
    def square(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
        v2.draw()

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
        v3.draw()

        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
        v4.draw()


    point0 = sd.get_point(200, 200)
    square(point=point0, angle=0, length=200)

elif f_input == 3:
    def pentagon(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
        v2.draw()

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
        v3.draw()

        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
        v4.draw()

        v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
        v5.draw()


    point0 = sd.get_point(200, 200)
    pentagon(point=point0, angle=0, length=200)
elif f_input == 4:
    def hexagon(point, angle, length):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()

        v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
        v2.draw()

        v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
        v3.draw()

        v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
        v4.draw()

        v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
        v5.draw()

        v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
        v6.draw()


    point0 = sd.get_point(200, 100)
    hexagon(point=point0, angle=0, length=200)
else:
    print('вы ввели некорректный номер')

sd.pause()
