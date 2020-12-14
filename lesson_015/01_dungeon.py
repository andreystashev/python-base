# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']

# TODO что то тут вам пайчарм подсказывает по поводу импортов
import re
import json
from csv import writer
from decimal import Decimal
from datetime import datetime


class Enemy:
    enemy_initialization = r'(Mob|Boss)_exp(\d+)_tm(\d+)'

    def initialize(self, enemy):
        finding_enemy = re.findall(self.enemy_initialization, enemy)
        health = int(finding_enemy[0][1])
        kill_time = Decimal(finding_enemy[0][2])
        return health, kill_time


class Location:
    location_initialization = r'(Location_\w+|Hatch)_tm([\d+|\d/.]+)'

    def initialize(self, location):
        finding_location = re.findall(self.location_initialization, location)
        name_location = finding_location[0][0]
        throw_time = Decimal(finding_location[0][1])
        return name_location, throw_time



# TODO В целом всё работает и работает верно
# TODO Но давайте теперь разбеерем все эти реализованные функции на разные классы
# TODO часть этой работы у вас уже начата.
# TODO Чтобы каждый класс занимался своими делами, отдельно от других. Это поможет и читаемость кода улучшить
# TODO И возможности для расширения увеличит.
# TODO Какие классы могут понадобиться?
# TODO 1) Локация - сюда можно поместить чтение внешнего файла, хранение текущей локации, смена текущей локации
# TODO ( + парсинг данных с регуляркой)
# TODO 2) Герой - тут можно учитывать состояние героя, его опыт, оставшееся время, проверять жив ли он
# TODO (кончилось ли время)
# TODO 3) Монстр - в таких объектах можно будет хранить опыт+время, состояние (жив/мертв, можно будет вметсо удаления
# TODO из списка использовать, или проверять и удалять мертвы)
# TODO 4) Игра - общий класс, регулирующий взаимодействие всех остальных. Тут будет выбор пользователя
# TODO и запуск нужных методов и всё остальное что нужно.

class Game:

    def __init__(self, remining_time, csv_names):
        # TODO не обязательно указывать что это class в названии.
        self.enemy_class = Enemy()
        self.location_class = Location()
        self.current_experience = 0
        self.elapsed_time = 0
        self.remaining_time = Decimal(remining_time)
        with open('dungeon.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = writer(csv_file, )
            csv_writer.writerow(csv_names)

    def turning(self, locations_branching, killed_enemies, enemies):
        locations = []
        for current_location, environment_in in locations_branching.items():
            if environment_in == "You are winner":
                return 'You are winner'
            for item in environment_in:
                if isinstance(item, dict):
                    locations.append(item)
                elif isinstance(item, str):
                    if not killed_enemies:
                        enemies.append(item)
            return current_location, enemies, locations

    def current_state(self, current_location, enemies, locations):
        with open('dungeon.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = writer(csv_file, )
            available_actions = []
            if enemies:
                available_actions.append("Уничтожить врага")
            if locations:
                available_actions.append("Сходить в другую локацию")
            available_actions.append("Выиграть игру")

            csv_writer.writerow([current_location, self.current_experience, datetime.now()])

            print(f" Вы сейчас в {current_location} и у вас {self.current_experience} опыта. ")
            print(f"До наводнения {self.remaining_time} секунд.")
            print(f"{self.elapsed_time} времени уже прошло.")
            showing_enemies = list(map(lambda enm: '- Враг: ' + enm, enemies))
            showing_locations = list(map(lambda loc: '- Вход в локацию: ' + list(loc.keys())[0], locations))
            print("Перед вами:")
            print(*showing_enemies, sep='\n')
            print(*showing_locations, sep='\n')
            print(f"Пришло время выбора:")
            available_actions = list(map(lambda act:
                                         str(available_actions.index(act) + 1)
                                         + '.'
                                         + act,
                                         available_actions))
            print(*available_actions, sep='\n')
            return available_actions

    def choising(self, action_length):
        available_choices = [str(i + 1) for i in range(action_length)]
        while True:
            option = input('Какое действие выберете? : ')
            if option in available_choices:
                break
        return option

    def killing(self, enemies):
        print('Доступные для уничтожения враги:')
        attacking_enemies = []
        for i in range(len(enemies)):
            attacking_enemies.append(str(i + 1) + '.' + enemies[i])
        print(*attacking_enemies, sep='\n')
        choose = self.choising(len(enemies))
        exp, tm = self.enemy_class.initialize(enemies[int(choose) - 1])
        self.current_experience += exp
        self.elapsed_time += tm
        self.remaining_time -= tm
        return choose

    def step_into_location(self, locations):
        print('Доступные для входа локации:')
        locations_for_action = \
            list(map(lambda x:
                     str(locations.index(x) + 1)
                     + '.Пройти в локацию: '
                     + list(x.keys())[0],
                     locations))
        print(*locations_for_action, sep='\n')
        choose = self.choising(len(locations))

        curr_location, tm = self.location_class.initialize(locations_for_action[int(choose) - 1])
        self.remaining_time -= tm
        self.elapsed_time += tm

        return choose

    def process(self):
        enemies_scope = []
        killed_enemies = False
        with open('rpg.json', 'r', encoding='utf8') as rpg:
            locations_branching = json.load(rpg)
        while True:
            turn = self.turning(locations_branching, killed_enemies, enemies_scope)
            if turn == 'You are winner':
                if self.current_experience >= 280:
                    print(turn)
                    return "win"
                else:
                    print('Вы слишком быстро добрались до выхода и чтобы доказать своё превосходство решаете '
                          'вернуться к началу и еще раз всех уничтожить')
                    return
            else:
                current_location, enemies, locations = turn
                if not locations or self.remaining_time <= 0:
                    print('Вы слишком быстро добрались до выхода и чтобы доказать своё превосходство решаете '
                          'вернуться к началу и еще раз всех уничтожить')
                    return
                todo_choice = self.current_state(current_location, enemies, locations)

                action = self.choising(len(todo_choice))
                action = todo_choice[int(action) - 1][2:]
                if action == 'Уничтожить врага':
                    dead_enemy = int(self.killing(enemies_scope)) - 1
                    enemies_scope.remove(enemies_scope[dead_enemy])
                    killed_enemies = True
                elif action == 'Сходить в другую локацию':
                    location_choice = int(self.step_into_location(locations)) - 1
                    next_location = locations[location_choice]
                    locations_branching = next_location
                    killed_enemies = False
                    enemies_scope = []
                elif action == 'Выиграть игру':
                    print('Вы решили подождать наводнения и волной вас вынесло к выходу.')
                    return 'exit'

    def go(self):
        while True:
            win = self.process()
            if win in ['win', 'exit']:
                print('Прекрасная игра! Вы выходите победителем.')
                break


game = Game(remining_time=remaining_time, csv_names=field_names)
game.go()

# Учитывая время и опыт, не забывайте о точности вычислений!

# TODO в конце нужно принтануть сколько времени осталось у игрока, когда он выйграл и когда он проиграл.
