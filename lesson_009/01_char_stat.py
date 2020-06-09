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
    letters_list = []
    numbers_list = []

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
            print('+{txt:-^30}+'.format(txt='+'))
            print('|{txt:^14}|'.format(txt='буква'), '{txt:^14}|'.format(txt='частота'))
            for line in file:
                for char in line:
                    if self.prev_char in self.stat:
                        if char in self.stat[self.prev_char]:
                            if char.isalpha() is True:
                                self.stat[self.prev_char][char] += 1
                        elif char.isalpha() is True:
                            self.stat[self.prev_char][char] = 1
                    else:
                        self.stat[self.prev_char] = {char: 1}
            print('+{txt:-^30}+'.format(txt='+'))

    def statistic(self):
        for _, count in self.stat.items():
            for letters, numbers in count.items():
                self.letters_list.append(letters)
                self.sort()
                self.numbers_list.append(numbers)
                for char_counts in self.numbers_list:
                    self.char_summa += char_counts
            for char in self.letters_list:
                count.get(char)
                print('|{txt:^14}|'.format(txt=char), '{txt:^14}|'.format(txt=count.get(char)))
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))

    def count_statistic(self):
        for _, count in self.stat.items():
            count = dict(zip(count.values(), count.keys()))
            for letters, numbers in count.items():
                self.letters_list.append(letters)
                self.sort()
                self.numbers_list.append(letters)
                for char_counts in self.numbers_list:
                    self.char_summa += char_counts
            for char in self.letters_list:
                count.get(char)
                print('|{txt:^14}|'.format(txt=count.get(char)), '{txt:^14}|'.format(txt=char))
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))

    def sort(self):
        pass


class Countmin(Counter):
    def sort(self):
        self.letters_list.sort()


class Countmax(Counter):
    def sort(self):
        self.letters_list.sort(reverse=True)


class Lettersmin(Counter):
    def sort(self):
        self.letters_list.sort()


class Lettersmax(Counter):
    def sort(self):
        self.letters_list.sort(reverse=True)


# sort_method = Countmin(zip_file_name='/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip')
# sort_method.unzip()
# sort_method.initialise(file_name='voyna-i-mir.txt')
# sort_method.count_statistic()

# sort_method = Countmax(zip_file_name='/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip')
# sort_method.unzip()
# sort_method.initialise(file_name='voyna-i-mir.txt')
# sort_method.count_statistic()


# sort_method = Lettersmin(zip_file_name='/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip')
# sort_method.unzip()
# sort_method.initialise(file_name='voyna-i-mir.txt')
# sort_method.statistic()

sort_method = Lettersmax(
    zip_file_name='/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip')
sort_method.unzip()
sort_method.initialise(file_name='voyna-i-mir.txt')
sort_method.statistic()

#  Хорошо, теперь применим паттерн "Шаблонный метод"
#  То есть в базовом классе оставить метод для получения отсортированной статистики пустым,
#  а потом сделать его наследников, в которых переопределить этот метод соответствующим образом

# Смотрите, у вас во всех наследниках код по сути одинаковый, отличается только сортировка статистики.
#  То есть у вас есть базовый класс, в котором определены методы -
#    1. раззиповать архив()
#    2. собрать словарь со статистикой()
#    Эти два метода у вас уже есть
#    3. распечатать эту статистику в таблице()
#         внутри этого метода нужно отсортировать статистику (вызвать метод sort())
#         и в цикле ее распечатать, обернув в таблицу
#    4. def sort():
#       pass
#   Так вот именно метод сортировки у вас будет переопределяться в наследниках. Сам метод печатания таблички
#   ничем отличаться не будет, так что его достаточно определить только в базов классе.
#   То есть в базовом классе мы оставляем этот метод пустым, затем в наследниках переопределяем только его, допустим
#   для LettersPlus это будет выглядеть так -
#   LettersMin(Counter):
#       def sort():
#            self.stat.sort(reverse=True)
#   В остальных наследниках аналогичная логика - только соритруем словарь нужным образом
#   И при вызове метда распечатки таблицы у нас будет осуществлена сортировка словаря нужным образом

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
