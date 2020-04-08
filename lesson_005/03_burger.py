# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from my_burger import (bread as add_bread, cutlet as add_cutlet, mayo as add_mayo,
                       cucumber as add_cucumber, cheese as add_cheese, tomato as add_tomato)

#  Ну можно было все-таки названия функций в my_burger поменять и так с импортом не извращаться)

add_bread()
add_cutlet()
add_mayo()
add_cucumber()
add_cutlet()
add_cheese()
add_tomato()
add_bread()

# зачет!
