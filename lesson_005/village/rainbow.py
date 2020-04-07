import simple_draw as sd

sd.resolution = (1200, 600)


def rainbow(point, step):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    radius = 1050
    for color in rainbow_colors:
        radius -= step

        sd.circle(center_position=point, radius=radius, color=color, width=19)


# TODO Этого кода не нужно. Кода вы импортируете модуль, вы импортируете весь код из него и при импорте он будет
#   выполнен. Можете для наглядности закомментировать вызов радуги в 04_painting, и увидите, что радуга все равно
#   там нарисуется. Чтобы код выполнялся только когда вызывается текущий модуль,
#   но не при импорте, можно обернуть его в такую конструкцию
#   if __name__ == '__main__':
#   Аналогично с выставлением разрешения для окна рисования.
#   Ну и в остальных модулях из этого пакета тоже нужно это поправить.
point = sd.get_point(400, -250)
rainbow(point=point, step=10)
