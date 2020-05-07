# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
try:
    BRUCE_WILLIS = 5
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as first_error:
    print(f'пятый элемент может быть только числом. Суть ошибки: {first_error}')
except IndexError as second_error:
    print(f'пятый элемент не содержит числа. Суть ошибки: {second_error}')
except NameError as third_error:
    print(f'Уиллис может быть только числом. Суть ошибки: {third_error}')
except:
    print('что-то пошло не так')


# зачет!




