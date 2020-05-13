# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile

# TODO В задании есть пункт - делать на классах

zip_file_name = '/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip'

zfile = zipfile.ZipFile(zip_file_name, 'r')
for filename in zfile.namelist():
    zfile.extract(filename)

file_name = 'voyna-i-mir.txt'
stat = {}


def initialise():
    prev_char = 'A'
    with open(file_name, 'r', encoding='cp1251') as file:
        for line in file:
            # print(line)
            for char in line:
                if prev_char in stat:
                    if char in stat[prev_char]:
                        if char.isalpha() is True:
                            stat[prev_char][char] += 1
                    elif char.isalpha() is True:
                        stat[prev_char][char] = 1
                else:
                    stat[prev_char] = {char: 1}

# TODO Хотелось бы видеть еще работу над неймингом - это важно. Не просто list_x, list_y, summa, sort_a и т.п,
#  а осмысленные имена, чтобы было сразу понятно, для чего нужны эти перменные/функции/классы.
def sort_a():
    for _, count in stat.items():
        list_x = []
        list_y = []
        for x, y in count.items():
            list_x.append(x)
            list_x.sort()
            summa = 0
            list_y.append(y)
            for i in list_y:
                summa += i
        for z in list_x:
            count.get(z)
            print('|{txt:^14}|'.format(txt=z), '{txt:^14}|'.format(txt=count.get(z)))
    print('+{txt:-^30}+'.format(txt='+'))
    print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=summa))
    print('+{txt:-^30}+'.format(txt='+'))


def sort_z():
    for _, count in stat.items():
        list_x = []
        list_y = []
        for x, y in count.items():
            list_x.append(x)
            list_x.sort(reverse=True)
            summa = 0
            list_y.append(y)
            for i in list_y:
                summa += i
        for z in list_x:
            count.get(z)
            print('|{txt:^14}|'.format(txt=z), '{txt:^14}|'.format(txt=count.get(z)))
    print('+{txt:-^30}+'.format(txt='+'))
    print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=summa))
    print('+{txt:-^30}+'.format(txt='+'))


def sort_01():
    for _, count in stat.items():
        list_x = []
        list_y = []
        count = dict(zip(count.values(), count.keys()))
        for x, y in count.items():
            list_x.append(x)
            list_x.sort()
            summa = 0
            list_y.append(x)
            for i in list_y:
                summa += i
        for z in list_x:
            count.get(z)
            print('|{txt:^14}|'.format(txt=count.get(z)), '{txt:^14}|'.format(txt=z))
    print('+{txt:-^30}+'.format(txt='+'))
    print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=summa))
    print('+{txt:-^30}+'.format(txt='+'))


def sort_99():
    for _, count in stat.items():
        list_x = []
        list_y = []
        count = dict(zip(count.values(), count.keys()))
        for x, y in count.items():
            list_x.append(x)
            list_x.sort(reverse=True)
            summa = 0
            list_y.append(x)
            for i in list_y:
                summa += i
        for z in list_x:
            count.get(z)
            print('|{txt:^14}|'.format(txt=count.get(z)), '{txt:^14}|'.format(txt=z))
    print('+{txt:-^30}+'.format(txt='+'))
    print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=summa))
    print('+{txt:-^30}+'.format(txt='+'))


print('+{txt:-^30}+'.format(txt='+'))
print('|{txt:^14}|'.format(txt='буква'), '{txt:^14}|'.format(txt='частота'))
print('+{txt:-^30}+'.format(txt='+'))

initialise()

sort_01()
# sort_99()
# sort_a()
# sort_z()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
