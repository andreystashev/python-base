# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


point1 = sd.get_point(50, 50)
point2 = sd.get_point(350, 450)

for color in rainbow_colors:
    point1.x += 5
    point2.x += 5
    sd.line(start_point=point1, end_point=point2, color=color, width=4)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


def rainbow(point, step):
    radius = 600
    for color in rainbow_colors:
        radius -= step

        sd.circle(center_position=point, radius=radius, color=color, width=19)


point = sd.get_point(300, -150)
rainbow(point=point, step=20)

sd.pause()

# зачет!

