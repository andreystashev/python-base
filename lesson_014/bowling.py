from state import Bowling, BothMove



def get_score(game_result):
    analysed_res = {}
    frames = 0
    for _ in game_result:
        for key, value in enumerate(zip(game_result.replace('X', 'X-')[0::2], game_result.replace('X', 'X-')[1::2]),
                                    start=1):
            analysed_res[key] = value
    for number, analysed_value in analysed_res.items():
        frames += 1
        if not analysed_value[0].isdigit() and analysed_value[0] != '-' and analysed_value[0] != 'X':
            if not analysed_value[1].isdigit() and analysed_value[1] and '/' or analysed_value[1] != '-':
                raise ValueError('Введено неправильное значение')
        if '0' in analysed_value:
            raise ValueError('Введено неправильное значение')

        elif '/' in analysed_value[0]:
            raise ValueError('Spare на первом броске')
        elif 'X' in analysed_value[1]:
            raise ValueError('Strike на втором броске')
        elif analysed_value[0].isdigit() and analysed_value[1].isdigit() and int(analysed_value[0]) + int(
                analysed_value[1]) >= 10:
            raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    # TODO Я изначально подумал, что состояние применяется к первому и второму ходу, и два разных класса, порожденных
    #  от одного это и есть состояние. И они не переключаются между собой а вызываются раздельно. Я так понял, одно состояние
    #  это два хода вместе, и второе состояние - функция, которая была ранее? Я ее внес в код, но не пойму как правильно
    #  переключить
    for score in [game_result]:
        game = Bowling()
    for throw_result in score:
        game.throw(throw_result)
    game.change_state(BothMove.num(analysed_value))
    return game.score


# result = 'XXXXXXXXXX'
# get_score(result)