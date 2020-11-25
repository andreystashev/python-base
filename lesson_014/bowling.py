analysed_res = {}
total = 0


def get_score(game_result):
    global analysed_res, total
    analysed_res = {}
    total = 0
    frames = 0
    for _ in game_result:
        for key, value in enumerate(zip(game_result.replace('X', 'X-')[0::2], game_result.replace('X', 'X-')[1::2]),
                                    start=1):
            analysed_res[key] = value
    for number, analysed_value in analysed_res.items():
        frames += 1
        result_count(analysed_value)
        if '0' in analysed_value:
            raise ValueError('Введено неправильное значение')
        elif '/' in analysed_value[0]:
            raise ValueError('Spare на первом броске')
        elif 'X' in analysed_value[1]:
            raise ValueError('Strike на втором броске')
        if analysed_value[0].isdigit() and analysed_value[1].isdigit() and int(analysed_value[0]) + int(
                analysed_value[1]) >= 10:
            raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def result_count(analysed_value):
    global total
    if 'X' in analysed_value:
        total += 20
    elif '/' in analysed_value:
        total += 15
    elif '-' in analysed_value:
        total += 0
    else:
        total += int(analysed_value[0]) + int(analysed_value[1])
    return analysed_value
