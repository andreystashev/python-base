# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Air:

    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other)

        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other)

        elif isinstance(other, Ground):
            return Dust(part1=self, part2=other)


class Water:

    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)

        elif isinstance(other, Ground):
            return Dirt(part1=self, part2=other)

        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other)


class Fire:

    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava(part1=self, part2=other)

        elif isinstance(other, Air):
            return Lightning(part1=self, part2=other)

        elif isinstance(other, Water):
            return Steam(part1=self, part2=other)


class Ground:

    def __str__(self):
        return 'Ground'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava(part1=self, part2=other)

        elif isinstance(other, Water):
            return Dirt(part1=self, part2=other)

        elif isinstance(other, Air):
            return Dust(part1=self, part2=other)

class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Storm = ' + str(self.part1) + ' + ' + str(self.part2)


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Lava = ' + str(self.part1) + ' + ' + str(self.part2)


class Dirt:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Dirt = ' + str(self.part1) + ' + ' + str(self.part2)


class Lightning:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Lightning = ' + str(self.part1) + ' + ' + str(self.part2)


class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Steam = ' + str(self.part1) + ' + ' + str(self.part2)

class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Dust = ' + str(self.part1) + ' + ' + str(self.part2)


air = Air()
water = Water()
fire = Fire()
ground = Ground()

result = air + water
print(result)

result = fire + ground
print(result)

result = water + ground
print(result)

result = air + fire
print(result)

result = water + fire
print(result)

result = air + ground
print(result)
# зачет!