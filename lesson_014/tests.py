import unittest

# TODO рекомендации, почему не нужно вставлять lesson_014 (на примере lesson_006) приведены тут https://clck.ru/Ndwqz
from lesson_014.bowling import get_score


# TODO тестов долно быть гораздо больше, охватить все случае, напишите примерно 15-17 тестов,
# TODO нужно делать тесты на исключения также.
class MySortTest(unittest.TestCase):
    def test_strikes(self):
        result = get_score(game_result='XXXXXXXXXX')
        # TODO для чего у вас написано это сообщение ? подсчет же верный
        self.assertEqual(result, 200, 'неверный подстчет страйков')

    def test_spares(self):
        result = get_score(game_result='-/-/-/-/-/-/-/-/-/-/')
        # TODO для чего у вас написано это сообщение ? подсчет же верный
        self.assertEqual(result, 150, 'неверный подсчет спэров')

    def test_numbers(self):

        result = get_score(game_result='11111111111111111111')
        self.assertEqual(result, 20, 'неверный подсчет чисел')


if __name__ == '__main__':
    unittest.main()

# TODO дописать тесты на переполнение, на недополнение, на ноль! + такие тесты как к примеру:
# TODO 'X4/341412X513/1-X'
# TODO 'X4/-41-12X5-3/1--9'
# TODO '99999999999999999999'
# TODO 'X4/-41-79X5-3/1--9'
# TODO '--------------------'
# TODO '-/-/-/-/-/-/-/-/-/-/'
# TODO 'XXXXXXXXXX'
# TODO '2/4/6/8/1/3/5/7/9/1/'
# TODO '/2/4/6/8/1/3/5/7/9/1'
# TODO 'qwerasdfzxcvtyghbnui'
# TODO '2/4/6/8/1/3/5/7/9/1/X'
# TODO '2/4/6/8/1/3/5/7/9/1'
# TODO ''
# TODO чем больше тестов тем лучше

