# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
#paper_x, paper_y = 8, 9

# проверить для
#paper_x, paper_y = 9, 8
paper_x, paper_y = 6, 8
paper_x, paper_y = 8, 6
paper_x, paper_y = 3, 4
#paper_x, paper_y = 11, 9
#paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)
if envelop_x > paper_x and envelop_y > paper_y \
        or envelop_y > paper_x and envelop_x > paper_y:
    print ('Да')
else:
    print ('Нет')
#todo раскоментировал ту бумагу, которая поместится

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
#brick_x, brick_y, brick_z = 11, 10, 2
#brick_x, brick_y, brick_z = 11, 2, 10
#brick_x, brick_y, brick_z = 10, 11, 2
#brick_x, brick_y, brick_z = 10, 2, 11
#brick_x, brick_y, brick_z = 2, 10, 11
#brick_x, brick_y, brick_z = 2, 11, 10
brick_x, brick_y, brick_z = 3, 5, 6
brick_x, brick_y, brick_z = 3, 6, 5
brick_x, brick_y, brick_z = 6, 3, 5
brick_x, brick_y, brick_z = 6, 5, 3
brick_x, brick_y, brick_z = 5, 6, 3
brick_x, brick_y, brick_z = 5, 3, 6
brick_x, brick_y, brick_z = 11, 3, 6
brick_x, brick_y, brick_z = 11, 6, 3
brick_x, brick_y, brick_z = 6, 11, 3
brick_x, brick_y, brick_z = 6, 3, 11
brick_x, brick_y, brick_z = 3, 6, 11
brick_x, brick_y, brick_z = 3, 11, 6
brick_x, brick_y, brick_z = 8, 9, 10
# (просто раскоментировать нужную строку и проверить свой код)


if 9 >= brick_x and 8 >= brick_y \
        or 9 >= brick_x and 8 >= brick_z  \
        or 9 >= brick_y and 8 >= brick_z \
        or 8 >= brick_y and 9 >= brick_z \
        or 8 >= brick_x and 9 >= brick_y \
        or 8 >= brick_x and 9 >= brick_z:
    print ('Да')
else:
    print('Нет')

#todo возможно не совсем так как задуманно решил. Включил в список последний кирпич
# (без него в этом списке можно было c одной восьмеркой без учета 9ки и последних 2х or вычислить)
# с гранями 8 и 9 для проверки и перебрал варианты где любые 2 грани у кирпича будут равны или меньше 8 и 9,
# раскоментировал те варианты которые пройдут в отверстие. Вместо переменных хол х хол у указал просто их значения чтобы
# проще выгдядело