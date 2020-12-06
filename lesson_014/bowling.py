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

    # TODO из примера https://refactoring.guru/ru/design-patterns/state
    # TODO у вас должен быть констекст, где как раз и будет реализован механизм переключения и само состояние.from
    # TODO До цикла нужно обявить класс констекст и передать в него первое состояние, и результат для анализа.

    # TODO что тут может быть далее, как вариант это while цикл пока есть результат для подсчета,
    # TODO в состояниях вы будите методом pop брать элементы для анализа,

    # TODO в цикле у вас вызов сначала первой функции и второй для обработки данных игры, эти функции должны быть
    # TODO должны быть определены в констексте
    # TODO переключение состояний должно быть в самом модуле state

    # TODO что за запись [game_result] ?
    for score in [game_result]:
        game = Bowling()
    for throw_result in score:
        game.throw(throw_result)
    game.change_state(BothMove.num(analysed_value))
    return game.score


# result = 'XXXXXXXXXX'
# get_score(result)