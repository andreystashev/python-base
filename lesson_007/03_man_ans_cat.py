# -*- coding: utf-8 -*-

from random import randint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            print('{} нет еды'.format(self.name))
            self.fullness -= 10

    def scratch(self):
        print('{} подрал обои'.format(self.name))
        self.house.dirt += 5
        self.fullness -= 10

    def sleep(self):
        print('{} лег спать'.format(self.name))
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} попал в дом'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.scratch()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.man_food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.man_food -= 10
        else:
            print('{} нет еды'.format(self.name))
            self.fullness -= 10

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        print('{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10

    def clean(self):
        print('{} убирал грязь'.format(self.name))
        self.fullness -= 20
        self.house.dirt -= 100

    def cat_shopping(self):
        if self.house.money >= 50:
            print('{} купил коту еды'.format(self.name))
            self.house.money -= 50
            self.house.cat_food += 50

        else:
            print('{} деньги кончились!'.format(self.name))

    def man_shopping(self):
        if self.house.money >= 50:
            print('{} купил коту еды'.format(self.name))
            self.house.money -= 50

            self.house.man_food += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} оставил котов'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.man_food < 30:
            self.man_shopping()
        elif self.house.cat_food < 30:
            self.cat_shopping()
        elif self.house.money < 100:
            self.work()
        elif self.house.dirt > 100:
            self.clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.cat_shopping()
        elif dice == 4:
            self.man_shopping()

        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.man_food = 50
        self.cat_food = 0
        self.dirt = 0
        self.money = 100

    def __str__(self):
        return 'В доме еды для человека осталось {},В доме еды кота осталось {}, грязи стало {}, денег стало {}'.format(
            self.man_food, self.cat_food, self.dirt, self.money)


citizens = [
    Cat(name='Кот Василий'),
    Cat(name='Кот Мурзик'),
    Cat(name='Кот Снежок'),
    Man(name='Человек Юрий'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
