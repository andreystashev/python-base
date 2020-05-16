# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NamesError(Exception):
    pass


class MailError(Exception):
    pass


class AgeError(Exception):
    pass


#  Не пойму, как разделить на 2 функции правильно. В каждой не хватает нужных переменных, которые во второй,
#  и если разделять на разные функции то цикл не срабатывает
# TODO Не нужно одну в другую помещать, это будут 2 разные функции.
#  В одной у нас будет проверка строки, то есть что-то вроде
#   def check_line(line):
#      name, mail, age = line.split()
#      если name невалидет
#          raise NamesError(...)
#      если mail невалидет:
#          raise MailError(...)
#      если age невалидет:
#          raise AgeError(...)

# TODO А в другой мы в цикле проверяем каждую строку и обрабатываем исключения -
#   открыли файл
#   for line in file:
#       try:
#            check_line(line)
#        если поймали исключение - записали в плохой_лог
#        иначе - в хороший_лог

#  Нужно написать две функции -
#  в одной мы реализуем алгоритм валидации строки с выбрасыванием исключения
#  в другой заводим цикл по файлу, вилидируем строку, ловим исключения, заполняем выходные файлы.
# #  В таком виде просто странно получается - выбростили исключение, и тут же его обработали.
def processing():
    file_name = 'registrations.txt'
    file = open(file_name, mode='r')
    for line in file:
        def check():
            name, mail, age = line.split()
            if name.isalpha() is False:
                raise NamesError(f"имя неправильно - {line}")
            elif '@' not in mail or '.' not in mail:
                raise MailError(f"почта неправильна - {line}")
            elif int(age) > 99 or int(age) < 10:
                raise AgeError(f"возраст неправильный - {line}")
            else:
                file_name = 'registrations_good.probe.log'
                file = open(file_name, mode='a')
                file_content = line
                file.write(file_content)
                file.close()

        try:
            check()
        except (IndexError, NamesError, AgeError, MailError, ValueError) as error:
            file_name = 'registrations_bad.probe.log'
            file = open(file_name, mode='a')
            file_content = str(error) + ' '
            file.write(file_content)
            file.close()
