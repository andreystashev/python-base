#!/usr/bin/env python3
"""
Handler - функция, которая принимает на вход text (текст входящего сообщения) и context (dict), а возвращает bool:
True если шаг пройден, False если данные введены неправильно.
"""
import datetime
import re
from settings import cities, cities_scope

date = re.compile(r"^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$")
seat = re.compile(r'^[1-9]$')

target_cities = ("москва", "ростов", "тверь", "казань", "самара")
current_cities = ("анапа", "грозный", "екатеринбург", "оренбург", "коломна")
# todo не пойму как в эти переменные можно передать значения вводимые пользователем. Пробовал поместить их в настройки и
#  передавать из контекста вот так '{target_city}', но так не запускается код потому что диспетчеру не хватает данных.
#  Попытка сделать пустые переменные и переписать их во время выбора пользователя его ответами тоже не сработала
date1 = '23-01-2021'
targ_1 = 'москва'
targ_2 = 'анапа'


def dispatch(city1, city2):
    for town1 in target_cities:
        if city1[0:2] == town1[0:2]:
            key = str(town1)
    for town2 in current_cities:
        if city2[0:2] == town2[0:2]:
            value = cities_scope[town2]
            true_value = cities[value]
    choice_list = {}
    count = 1
    for date in true_value[key]:
        user_day, user_month, user_year = map(int, date1.split('-'))
        day, month, year = map(int, date.split('-'))
        if datetime.timedelta(year, month, day) > datetime.timedelta(user_year, user_month, user_day):
            choice_list[count] = date
            count += 1
    print(choice_list)


dispatch(city1=targ_1, city2=targ_2)


def handle_target_town(text, context):
    for city in target_cities:
        if text.lower()[0:4] == city[0:4]:
            context['target_city'] = text
            return True
    else:
        return False


def handle_current_town(text, context):
    for city in current_cities:
        if text.lower()[0:4] == city[0:4]:
            context['current_city'] = text
            return True
    else:
        return False


def handle_date(text, context):
    match = re.match(date, text)
    if match:
        context['date'] = text
        return True
    else:
        return False


def handle_fly_choice(text, context):
    if int(text) <= 5:
        context['flies'] = text
        # dispatch(city1=targ_1, city2=targ_2)
        return True
    else:
        return False


def handle_seats(text, context):
    if int(text) <= 5:
        context['seats'] = text
        return True
    else:
        return False


def handle_comment(text, context):
    return True


def handle_choice(text, context):
    if text == 'да':
        # context['result'] = ''
        return True
    else:
        # todo  не пойму какое условие прописать для выхода из сценария, хотел сделать шаг 10 в сценарии, на который можно
        #  попасть только отсюда, но не знаю возможно ли передать в сетиингс чтобы был выбор шага в зависимости от принятого
        #  решения здесь

        return False


def handle_phone(text, context):
    if int(text) <= 99999999999:
        context['phone'] = text
        return True
    else:
        return False
