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


file_name = 'registrations.txt'
file = open(file_name, mode='r')

for line in file:
    linelist = line.split()
    try:

        if linelist[0].isalpha() == False or ('@' or '.') not in linelist[1] or 10 > int(linelist[2]) > 99 or int(
                linelist[2]) < 10:
            file_name = 'registrations_bad.log'
            file = open(file_name, mode='a')

            if linelist[0].isalpha() == False:
                file_content = str('неверное имя - ') + line
                file.write(file_content)
            elif ('@' or '.') not in linelist[1]:
                file_content = str('неверная почта - ') + line
                file.write(file_content)
            else:
                file_content = str('неверный возраст - ') + line
                file.write(file_content)
            file.close()

        else:
            file_name = 'registrations_good.log'
            file = open(file_name, mode='a')
            file_content = line
            file.write(file_content)
            file.close()

    except IndexError as first_error:
        # print(f'Суть ошибки: {first_error}')
        file_name = 'registrations_bad.log'
        file = open(file_name, mode='a')
        file_content = str('Отсутствует элемент - ')+line
        file.write(file_content)
        file.close()


file.close()
