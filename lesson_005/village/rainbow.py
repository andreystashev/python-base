import simple_draw as sd


def rainbow(point, step):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    radius = 1050
    for color in rainbow_colors:
        radius -= step

        sd.circle(center_position=point, radius=radius, color=color, width=19)


# TODO "можно обернуть его в такую конструкцию
#   if __name__ == '__main__':
#   Аналогично с выставлением разрешения для окна рисования"
#     Эту строчку недопонял. Нужно к строчке sd.resolution подставлять if name = main, или удалять?
#     Я его подставлял только чтобы скорректировать отображение в каждой функции относительно 04_painting,
#     И их наличие или отсутствие на общей картине ничего не меняют по моим наблюдениям

if __name__ == '__main__':

    point = sd.get_point(400, -250)
    rainbow(point=point, step=10)
