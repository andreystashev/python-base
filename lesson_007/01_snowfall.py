# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    pass

    xpoint = sd.random_number(100, 500)
    ypoint = sd.random_number(500, 700)
    color = sd.COLOR_WHITE
    length = sd.random_number(15, 30)

    def clear_previous_picture(self):
        sd.snowflake(center=sd.get_point(flake.xpoint, flake.ypoint), length=flake.length, color=sd.background_color)

    def move(self):
        flake.ypoint -= 20

    def draw(self, color):
        sd.snowflake(center=sd.get_point(flake.xpoint, flake.ypoint), length=flake.length, color=color)

    def can_fall(self):
        if flake.ypoint <= 0:
            flake.ypoint += 600

    def get_flakes(self, count):
        global flakes
        flakes = []
        for _ in range(count):
            flakes.append(Snowflake)
        return flakes

    def get_fallen_flakes(self):
        flakes.reverse()
        for i in flakes:
            del flakes[i]

    def append_flakes(self):
        flakes.reverse()
        x = Snowflake
        for _ in flakes:
            flakes.append(x)



flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw(color=flake.color)
    if flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

     #todo с первой частью получилось заставить снежинку падать, не понял какое условие должно быть у
    #  функции flake.can_fall() Со вторым шагом уже запутался. Не пойму как правильно добавить в список саму снежинку
    #  и использовать функции из цикла без изменений

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = flake.get_flakes(count=5)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw(color=flake.color)
    fallen_flakes = flake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flake.append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
