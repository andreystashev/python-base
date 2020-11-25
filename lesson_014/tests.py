import unittest

from lesson_014.bowling import get_score


class MySortTest(unittest.TestCase):
    def test_strikes(self):
        result = get_score(game_result='XXXXXXXXXX')
        self.assertEqual(result, 200, 'неверный подстчет страйков')

    def test_spares(self):
        result = get_score(game_result='-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 150, 'неверный подсчет спэров')

    def test_numbers(self):
        result = get_score(game_result='11111111111111111111')
        self.assertEqual(result, 20, 'неверный подсчет чисел')

if __name__ == '__main__':
    unittest.main()