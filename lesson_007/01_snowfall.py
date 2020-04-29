# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

flakes = []


class Snowflake:
    def __init__(self):
        self.xpoint = sd.random_number(100, 500)
        self.ypoint = sd.random_number(600, 700)
        self.length = sd.random_number(15, 30)
        self.color = sd.COLOR_WHITE

    def clear_previous_picture(self):
        sd.snowflake(center=sd.get_point(flake.xpoint, flake.ypoint), length=flake.length, color=sd.background_color)

    def move(self):
        flake.ypoint -= 20

    def draw(self, color):
        sd.snowflake(center=sd.get_point(flake.xpoint, flake.ypoint), length=flake.length, color=color)

    def can_fall(self):
        if flake.ypoint <= 0:
            flake.ypoint += 600

    def get_fallen_flakes(self):
        if flake.ypoint <= 0:
            flake.draw(color=sd.background_color)

        global fallen_snow
        fallen_snow = []
        for i, value in enumerate(flakes):
            if flake.ypoint <= -100:
                fallen_snow.append(i)

        return fallen_snow

    def del_flakes(self):
        fallen_snow.reverse()
        for i in fallen_snow:
            del flakes[i]

    def append_flakes(self):
        fallen_snow.reverse()
        for _ in fallen_snow:
            flakes.append(Snowflake())

    def get_flakes(self, count):
        for _ in range(count):
            flakes.append(Snowflake())


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw(color=flake.color)
#     if flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flake.get_flakes(count=7)  # создать список снежинок
while True:

    for flake in flakes:
        sd.start_drawing()
        flake.clear_previous_picture()
        flake.move()
        flake.draw(color=flake.color)
        flake.get_fallen_flakes()
        flake.del_flakes()
        flake.append_flakes()
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

sd.pause()
