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
x_point = [100, 150, 200, 250, 300]
for x in x_point:
    length = sd.random_number(10, 100)
    y = sd.random_number(500, 700)
    snow1 = sd.get_point(x, y)
    snow2 = sd.get_point(x+100, y+400)
    snow3 = sd.get_point(x+200, y+100)
    snow4 = sd.get_point(x + 300, y +350)
    while True:
        sd.clear_screen()
        snow1.y -= 40
        snow2.y -= 40
        snow3.y -= 35
        snow4.y -= 40
        sd.snowflake(center=snow1, length=length)
        sd.snowflake(center=snow2, length=length / 2)
        sd.snowflake(center=snow3, length=length / 1.5)
        sd.snowflake(center=snow4, length=length / 2.5)

        sd.sleep(0.01)
        if snow1.y < -450:
            break
        if sd.user_want_exit():
            break
#todo я так понимаю, что задание подразумевает падение снежинок всех вместе. Не разобрался, как с помощью циклов
# это реализовать, у меня получалось, что падает только по 1 снежинке и следующая начинает падать, как только предыдущая
# приземлится. Вручную прописал 4 снежинки, чтобы появлялось по 4 сразу 5 циклов подряд.
sd.pause()

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


