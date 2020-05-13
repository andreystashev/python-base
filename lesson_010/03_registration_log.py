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

class nameError(Exception):
    pass


class mailError(Exception):
    pass


class ageError(Exception):
    pass


file_name = 'registrations.txt'
file = open(file_name, mode='r')

for line in file:

    try:
        linelist = line.split()
        name = linelist[0]
        mail = linelist[1]
        age = linelist[2]

        if name.isalpha() is False:
            raise nameError
        elif '@' not in mail or '.' not in mail:
            raise mailError
        elif int(age) > 99 or int(age) < 10:
            raise ageError


        else:
            file_name = 'registrations_good.probe.log'
            file = open(file_name, mode='a')
            file_content = line
            file.write(file_content)
            file.close()

    except IndexError as first_error:
        file_name = 'registrations_bad.probe.log'
        file = open(file_name, mode='a')
        file_content = str('Отсутствует элемент - ') + line
        file.write(file_content)
        file.close()
    except nameError as first_error:
        file_name = 'registrations_bad.probe.log'
        file = open(file_name, mode='a')
        file_content = str('имя неправильно - ') + line
        file.write(file_content)
        file.close()
    except mailError as second_error:
        file_name = 'registrations_bad.probe.log'
        file = open(file_name, mode='a')
        file_content = str('почта неверна - ') + line
        file.write(file_content)
        file.close()
    except ageError as third_error:
        file_name = 'registrations_bad.probe.log'
        file = open(file_name, mode='a')
        file_content = str('возраст неверен - ') + line
        file.write(file_content)
        file.close()

file.close()
