# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for x in range(-50, 1100, 100):
    x += 50
    left_bottom = sd.get_point(0 + x, 0)
    right_top = sd.get_point(100 + x, 50)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)
    for y in range(0, 1100, 100):
        y += 50
        left_bottom = sd.get_point(50 + x, 0 + y)
        right_top = sd.get_point(150 + x, 50 + y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)
    for z in range(0, 1100, 100):
        z += 100
        left_bottom = sd.get_point(0 + x, 0 + z)
        right_top = sd.get_point(100 + x, 50 + z)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)

#todo Исправил свой код, снизу сделал упрощенный по вашей схеме

# line = 0
# for y in range(0, 600, 50):
#     line += 1
#     for x in range(0, 600, 100):
#         if line % 2 == 0:
#             x += 50
#         left_bottom = sd.get_point(0 + x, 0 + y)
#         right_top = sd.get_point(100 + x, 50 + y)
#         sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=2)

sd.pause()
