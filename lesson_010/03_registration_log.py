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


#  Нужно написать две функции -
#  в одной мы реализуем алгоритм валидации строки с выбрасыванием исключения
#  в другой заводим цикл по файлу, вилидируем строку, ловим исключения, заполняем выходные файлы.
# #  В таком виде просто странно получается - выбростили исключение, и тут же его обработали.

def check_line(line):
    name, mail, age = line.split()
    if name.isalpha() is False:
        raise NamesError(f"имя неправильно - {line}")
    elif '@' not in mail or '.' not in mail:
        raise MailError(f"почта неправильна - {line}")
    elif int(age) > 99 or int(age) < 10:
        raise AgeError(f"возраст неправильный - {line}")


def processing(file_name):
    file_name = file_name
    file = open(file_name, mode='r')
    for line in file:
        try:
            check_line(line)
        except (IndexError, NamesError, AgeError, MailError, ValueError) as error:
            file_name = 'registrations_bad.probe.log'
            file = open(file_name, mode='a')
            file_content = str(error) + ' '
            file.write(file_content)
            file.close()
        else:
            file_name = 'registrations_good.probe.log'
            file = open(file_name, mode='a')
            file_content = line
            file.write(file_content)
            file.close()


processing(file_name='registrations.txt')