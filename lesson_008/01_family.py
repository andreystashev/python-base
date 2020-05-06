# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class House:

    def __init__(self):
        self.money = 100
        self.man_food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'Осталось денег {}, еды {}, грязи {}, еды кота {},'.format(
            self.money, self.man_food, self.dirt, self.cat_food)

    def act(self):
        self.dirt += 5


class Human:
    all_money = 0
    all_eat = 0
    total_coat = 0

    def __init__(self, name, sweet_home):
        self.name = name
        self.fullness = 30
        self.sanity = 100
        self.house = sweet_home

    def __str__(self):
        return 'Я - {}, сытость {}, рассудок {}'.format(
            self.name, self.fullness, self.sanity)

    def act(self):
        if self.fullness <= 0:
            print('{} умер(ла) от голода...'.format(self.name))
            return False

        if self.sanity <= 0:
            print('{} умер(ла) от страданий...'.format(self.name))
            return False
        if self.house.dirt > 90:
            self.sanity -= 5

        if self.house.man_food >= 20 and 0 <= self.fullness <= 30:
            print('{} поел(а)'.format(self.name))
            self.fullness += 20
            self.house.man_food -= 20
            self.all_eat += 20
            return False

        return True

    def play_cat(self):
        self.sanity += 5
        print('{} гладит кота'.format(self.name))
        self.fullness -= 10



class Husband(Human):
    def act(self):
        if super().act():
            dice = randint(1, 3)
            if self.house.man_food < 30:
                self.work()
            elif self.sanity < 30:
                self.gaming()
            elif self.house.money < 100:
                self.work()
            elif self.house.dirt > 100:
                self.gaming()
            elif dice == 1:
                self.gaming()
            elif dice == 2:
                self.play_cat()
            else:
                self.work()

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10
        self.all_money += 150

    def gaming(self):
        print('{} играл в WaT'.format(self.name))
        self.fullness -= 10
        self.sanity += 20


class Wife(Human):

    def act(self):
        if super().act():
            dice = randint(1, 5)
            if self.house.man_food <= 30:
                self.shopping()
            elif self.sanity < 30:
                self.buy_fur_coat()
            elif self.house.dirt > 100:
                self.clean_house()
            elif dice == 1:
                self.clean_house()
            elif dice == 2 and self.house.money > 500:
                self.buy_fur_coat()
            elif dice == 3 or murzik.fullness <= 40:
                self.cat_shopping()
            elif dice == 4:
                self.play_cat()
            else:
                self.shopping()

    def shopping(self):
        if self.house.money >= 50:
            print('{} купила еды'.format(self.name))
            self.house.money -= 50
            self.house.man_food += 50
            self.fullness -= 10
        else:
            print('{} деньги кончились!'.format(self.name))
            self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money >= 350:
            print('{} купила шубу'.format(self.name))
            self.house.money -= 350
            self.sanity += 60
            self.fullness -= 10
            self.total_coat += 1

    def clean_house(self):
        print('{} убрала грязь'.format(self.name))
        self.fullness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0

    def cat_shopping(self):
        if self.house.money >= 30:
            print('{} купила еды для кота'.format(self.name))
            self.house.money -= 30
            self.house.cat_food += 30
            self.fullness -= 10
        else:
            print('{} деньги кончились!'.format(self.name))
            self.fullness -= 10

# home = House()
# serge = Husband(name='Сережа', sweet_home=home)
# masha = Wife(name='Маша', sweet_home=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     home.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
# cprint('Шуб {}'.format(masha.total_coat), color='yellow')
# cprint('Денег {}'.format(serge.all_money), color='yellow')
# cprint('Съедено {}'.format(masha.all_eat + serge.all_eat), color='yellow')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, sweet_home):
        self.name = name
        self.fullness = 30
        self.house = sweet_home

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            print('{} умер'.format(self.name))
            return
        dice = randint(1, 4)
        if self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            self.fullness -= 10
            print('нет еды для кота')

    def sleep(self):
        print('{} лег спать'.format(self.name))
        self.fullness -= 10

    def soil(self):
        print('{} подрал обои'.format(self.name))
        self.house.dirt += 5
        self.fullness -= 10


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


class Child(Human):

    def __init__(self, name, sweet_home):
        self.name = name
        self.fullness = 30
        self.sanity = 100
        self.house = sweet_home

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 2)
        if self.fullness <= 30:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        if self.house.man_food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.man_food -= 10
            self.all_eat += 10
        else:
            print('{} нет еды'.format(self.name))
            self.fullness -= 10

    def sleep(self):
        print('{} лег спать'.format(self.name))
        self.fullness -= 10


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', sweet_home=home)
masha = Wife(name='Маша', sweet_home=home)
kolya = Child(name='Коля', sweet_home=home)
murzik = Cat(name='Мурзик', sweet_home=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    home.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
