import unittest

from bowling import get_score


class MySortTest(unittest.TestCase):
    def test_strikes(self):
        result = get_score(game_result='XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_spares(self):
        result = get_score(game_result='-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 150)

    def test_numbers(self):
        result = get_score(game_result='11111111111111111111')
        self.assertEqual(result, 20)

    def test_all_symbols(self):
        result = get_score(game_result='X4/341412X513/1-X')
        self.assertEqual(result, 112)

    def test_all_symbols1(self):
        result = get_score(game_result='X4/-41-12X5-3/1--9')
        self.assertEqual(result, 93)

    def test_nines(self):
        with self.assertRaises(ValueError):
            get_score(game_result='99999999999999999999')

    def test_nine(self):
        with self.assertRaises(ValueError):
            get_score(game_result='X4/-41-79X5-3/1--9')

    def test_zero_result(self):
        result = get_score(game_result='--------------------')
        self.assertEqual(result, 0)

    def test_spare(self):
        result = get_score(game_result='-/-/-/-/-/-/-/-/-/-/')
        self.assertEqual(result, 150)

    def test_spare_first(self):
        with self.assertRaises(ValueError):
            get_score(game_result='/2/4/6/8/1/3/5/7/9/1')

    def test_all_numbers(self):
        result = get_score(game_result='2/4/6/8/1/3/5/7/9/1/')
        self.assertEqual(result, 150)

    def test_letters(self):
        with self.assertRaises(ValueError):
            get_score(game_result='qwerasdfzxcvtyghbnui')

    def test_frames(self):
        with self.assertRaises(Exception):
            get_score(game_result='2/4/6/8/1/3/5/7/9/1/X')

    def test_frames2(self):
        with self.assertRaises(Exception):
            get_score(game_result='2/4/6/8/1/3/5/7/9/1')

    def test_nothing(self):
        with self.assertRaises(Exception):
            get_score(game_result='')

    def test_zero(self):
        with self.assertRaises(Exception):
            get_score(game_result='0')


if __name__ == '__main__':
    unittest.main()


