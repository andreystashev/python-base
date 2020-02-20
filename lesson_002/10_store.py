#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

desk_code = goods ['Стол']
desk_item = store[desk_code][0]
desk_item1 = store[desk_code][1]
desk_quantity = desk_item['quantity']
desk_quantity1 = desk_item1['quantity']
desk_price = desk_item['price']
desk_price1 = desk_item1['price']
desk_cost = desk_quantity * desk_price
desk_cost1 = desk_quantity1 * desk_price1
desk_money = desk_cost+desk_cost1
desk = desk_quantity + desk_quantity1
print ('Стол -', desk, 'шт, стоимость', desk_money, 'руб')


sofa_code = goods ['Диван']
sofa_item = store[sofa_code][0]
sofa_item1 = store[sofa_code][1]
sofa_quantity = sofa_item['quantity']
sofa_quantity1 = sofa_item1['quantity']
sofa_price = sofa_item['price']
sofa_price1 = sofa_item1['price']
sofa_cost = sofa_quantity * sofa_price
sofa_cost1 = sofa_quantity1 * sofa_price1
sofa_money = sofa_cost+sofa_cost1
sofa = sofa_quantity + sofa_quantity1
print ('Диван -', sofa, 'шт, стоимость', sofa_money, 'руб')


chair_code = goods ['Стул']
chair_item = store[chair_code][0]
chair_item1 = store[chair_code][1]
chair_item2 = store[chair_code][2]
chair_quantity = chair_item['quantity']
chair_quantity1 = chair_item1['quantity']
chair_quantity2 = chair_item2['quantity']
chair_price = chair_item['price']
chair_price1 = chair_item1['price']
chair_price2 = chair_item2['price']
chair_cost = chair_quantity * chair_price
chair_cost1 = chair_quantity1 * chair_price1
chair_cost2 = chair_quantity2 * chair_price2
chair_money = chair_cost+chair_cost1+chair_cost2
chair = chair_quantity + chair_quantity1 + chair_quantity2
print ('Стул -', chair, 'шт, стоимость', chair_money, 'руб')


# нет, особой необходимости в нем нет.

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################


# зачет!

