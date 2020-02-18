#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
my_family = ['father', 'mother', 'brother']
my_family_height = [['father', 200],['mother', 150], ['brother', 100]]

f = (my_family_height [0][1])
m = (my_family_height [1][1])
b = (my_family_height [2][1])
print ('Рост отца -', (my_family_height [0][1]), 'cm')

family_height = f+m+b
print ('Общий рост моей семьи -',(family_height), 'cm')

