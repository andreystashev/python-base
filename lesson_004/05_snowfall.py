# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# TODO Используем константу N, а не просто число 20.
#  И если переменная цикла не используется в самом цикле, ее принято _ (нижнее подчеркивание) называть.
x_point = [sd.random_number(10, 590) for i in range(20)]
y_point = [sd.random_number(0, 0) for i in range(20)]
length_list = [sd.random_number(10, 40) for i in range(20)]

# while True:
#
#     for i in range(N):
#
#         sd.start_drawing()
#         sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=l_list[i], color=sd.background_color)
#         y_point[i] -= 20
#         sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=l_list[i], color=sd.COLOR_WHITE)
#         sd.finish_drawing()
#
#         if y_point[i] < -30:
#             y_point[i] += sd.random_number(600, 1000)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

while True:

    for i in range(N):

        sd.start_drawing()
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.background_color)
        y_point[i] -= 30
        x_point[i] += sd.random_number(-30, 30)
        sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.COLOR_WHITE)
        sd.finish_drawing()

        if y_point[i] < 50:
            y_point[i] += sd.random_number(600, 1000)
            sd.snowflake(center=sd.get_point(x_point[i], y_point[i]), length=length_list[i], color=sd.COLOR_WHITE)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
