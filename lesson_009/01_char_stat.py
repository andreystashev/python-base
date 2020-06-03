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
        self.sort()
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt:^14}|'.format(txt='итого'), '{txt:^14}|'.format(txt=self.char_summa))
        print('+{txt:-^30}+'.format(txt='+'))

    def sort(self):
        # for _, count in self.stat.items():
        #     letters_list = []
        #     numbers_list = []
        #     for letters, numbers in count.items():
        #         letters_list.append(letters)
        #         letters_list.sort()
        #         numbers_list.append(numbers)
        #         for char_counts in numbers_list:
        #             self.char_summa += char_counts
        #     for char in letters_list:
        #         count.get(char)
        #         print('|{txt:^14}|'.format(txt=char), '{txt:^14}|'.format(txt=count.get(char)))
        pass
# Todo если раскомментировать sort из основного класса, то код работает. Но при попытке его сделать в методе другого класса
#  он никак не хочет срабатывать. Также при попытке разделить код из sort он не хочет работать, не могу выделить одну строчку
#  с которой можно было бы работать в наследниках

class LettersPlus(Counter):
    def __init__(self):
        super().__init__(self)

    def sort(self):
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


class LettersMin(Counter):
    def sort(self):
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


class CountPlus(Counter):
    def sort(self):
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


class CountMin(Counter):
    def sort(self):
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


counter = Counter(
    zip_file_name='/Users/andrey/PycharmProjects/python_base/lesson_009/python_snippets/voyna-i-mir.txt.zip'
)
counter.unzip()
counter.initialise(file_name='voyna-i-mir.txt')
l_plus = LettersPlus()
l_plus.sort()
counter.statistic()

#  Хорошо, теперь применим паттерн "Шаблонный метод"
#  То есть в базовом классе оставить метод для получения отсортированной статистики пустым,
#  а потом сделать его наследников, в которых переопределить этот метод соответствующим образом
#  не могу понять, как правильно сделать, чтобы наследники начали работать. В задании 8 модуля с семьей
#  похожий код работал, а тут не хватает какого-то кода. Пробовал через супер и деф __инит__ добавить, но
#  не дает результата. Пишет, что не хватает селф, но я не пойму почему здесь его требует а в задании с семьей
#  к примеру этого не было. И само это взаимодействие не понятно, в примере шаблона не разобрался, в интренете
#  тоже примеры описаны так что не могу уловить суть. Тоесть зачем метод, что он делает, и как он должен выглядеть
#  относительно понятно, а реализовать в коде не получается

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
