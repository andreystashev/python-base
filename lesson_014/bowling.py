
def get_score(game_result):
    # TODO пайчарм вам подсказывает что эти переменные он не может найти в глобальном скоупе
    global analized_res, total
    analized_res = {}
    total = 0
    frames = 0
    for _ in game_result:
        # TODO нейминг получаемых переменных старайтесь не сокращать их название
        for i, k in enumerate(zip(game_result.replace('X', 'X-')[0::2], game_result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    for k, v in analized_res.items():
        frames += 1
        result_count(v)
        if '0' in v:
            raise ValueError('Введено неправильное значение')
        elif '/' in v[0]:
            raise ValueError('Spare на первом броске')
        elif 'X' in v[1]:
            raise ValueError('Strike на втором броске')
        if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[1]) >= 10:
            raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')
    print(total)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total

# TODO что есть параметр "V" в данном случае ? из названия не понятно
def result_count(v):
    # TODO пайчарм вам подсказывает что эти переменные он не может найти в глобальном скоупе
    global total
    if 'X' in v:
        total += 20
    elif '/' in v:
        total += 15
    elif '-' in v:
        total += 0
    else:
        total += int(v[0]) + int(v[1])
    return v


