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


class Counter:
    prev_char = 'A'
    char_summa = 0

    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.zip_file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            return filename

    def initialise(self, file_name):
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                # print(line)
                for char in line:
                    if self.prev_char in self.stat:
                        if char in self.stat[self.prev_char]:
                            if char.isalpha() is True:
                                self.stat[self.prev_char][char] += 1
                        elif char.isalpha() is True:
                            self.stat[self.prev_char][char] = 1
                    else:
                        self.stat[self.prev_char] = {char: 1}

    def letters_increase(self):
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='буква'), '{txt:^14}|'.format(txt='частота'))
        print('+{txt:-^30}+'.format(txt='+'))
        for _, count in self.stat.items():
            letters_list = []
            numbers_list = []
            for letters, numbers in count.items():
                letters_list.append(letters)
                letters_list.sort()
                numbers_list.append(numbers)
                for char_counts in numbers_list:
                    self.char_summa += char_counts
            for char in letters_list:
                count.get(char)
                print('|{txt:^14}|'.format(txt=char), '{txt:^14}|'.format(txt=count.get(char)))
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))

    def letters_decrease(self):
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='буква'), '{txt:^14}|'.format(txt='частота'))
        print('+{txt:-^30}+'.format(txt='+'))
        for _, count in self.stat.items():
            letters_list = []
            numbers_list = []
            for letters, numbers in count.items():
                letters_list.append(letters)
                letters_list.sort(reverse=True)
                numbers_list.append(numbers)
                for char_counts in numbers_list:
                    self.char_summa += char_counts
            for char in letters_list:
                count.get(char)
                print('|{txt:^14}|'.format(txt=char), '{txt:^14}|'.format(txt=count.get(char)))
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))

    def count_increase(self):
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='буква'), '{txt:^14}|'.format(txt='частота'))
        print('+{txt:-^30}+'.format(txt='+'))
        for _, count in self.stat.items():
            letters_list = []
            numbers_list = []
            count = dict(zip(count.values(), count.keys()))
            for letters, numbers in count.items():
                letters_list.append(letters)
                letters_list.sort()
                numbers_list.append(letters)
                for char_counts in numbers_list:
                    self.char_summa += char_counts
            for char in letters_list:
                count.get(char)
                print('|{txt:^14}|'.format(txt=count.get(char)), '{txt:^14}|'.format(txt=char))
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))

    def count_decrease(self):
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='буква'), '{txt:^14}|'.format(txt='частота'))
        print('+{txt:-^30}+'.format(txt='+'))
        for _, count in self.stat.items():
            letters_list = []
            numbers_list = []
            count = dict(zip(count.values(), count.keys()))
            for letters, y in count.items():
                letters_list.append(letters)
                letters_list.sort(reverse=True)

                numbers_list.append(letters)
                for char_counts in numbers_list:
                    self.char_summa += char_counts
            for char in letters_list:
                count.get(char)
                print('|{txt:^14}|'.format(txt=count.get(char)), '{txt:^14}|'.format(txt=char))
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))


counter = Counter(
    zip_file_name='/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip'
)
counter.unzip()
counter.initialise(file_name='voyna-i-mir.txt')
counter.count_increase()
# counter.count_decrease()
# counter.letters_increase()
# counter.letters_decrease()

# TODO Хорошо, теперь применим паттерн "Шаблонный метод"
#  То есть в базовом классе оставить метод для получения отсортированной статистики пустым,
#  а потом сделать его наследников, в которых переопределить этот метод соответствующим образом


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
