import unittest

from bowling import get_score


class MySortTest(unittest.TestCase):

    def test_strikes(self):
        result = get_score(game_result='XXXXXXXXXX',state='self')
        self.assertEqual(result, 200)

    def test_spares(self):
        result = get_score(game_result='-/-/-/-/-/-/-/-/-/-/',state='self')
        self.assertEqual(result, 150)

    def test_numbers(self):
        result = get_score(game_result='11111111111111111111',state='self')
        self.assertEqual(result, 20)

    def test_all_symbols(self):
        result = get_score(game_result='X4/341412X513/1-X',state='self')
        self.assertEqual(result, 112)

    def test_all_symbols1(self):
        result = get_score(game_result='X4/-41-12X5-3/1--9',state='self')
        self.assertEqual(result, 93)

    def test_nines(self):
        with self.assertRaises(ValueError):
            get_score(game_result='99999999999999999999',state='self')

    def test_nine(self):
        with self.assertRaises(ValueError):
            get_score(game_result='X4/-41-79X5-3/1--9',state='self')

    def test_zero_result(self):
        result = get_score(game_result='--------------------',state='self')
        self.assertEqual(result, 0)

    def test_spare_first(self):
        with self.assertRaises(ValueError):
            get_score(game_result='/2/4/6/8/1/3/5/7/9/1',state='self')

    def test_all_numbers(self):
        result = get_score(game_result='2/4/6/8/1/3/5/7/9/1/',state='self')
        self.assertEqual(result, 150)

    def test_letters(self):
        with self.assertRaises(ValueError):
            get_score(game_result='qwerasdfzxcvtyghbnui',state='self')

    def test_frames(self):
        with self.assertRaises(Exception):
            get_score(game_result='2/4/6/8/1/3/5/7/9/1/X',state='self')

    def test_frames2(self):
        with self.assertRaises(Exception):
            get_score(game_result='2/4/6/8/1/3/5/7/9/1',state='self')

    def test_nothing(self):
        with self.assertRaises(Exception):
            get_score(game_result='',state='self')

    def test_zero(self):
        with self.assertRaises(Exception):
            get_score(game_result='0',state='self')


    def test_strikes_market(self):
        result = get_score(game_result='XXXXXXXXXX',state='market')
        self.assertEqual(result, 270)

    def test_numbers_market(self):
        result = get_score(game_result='11111111111111111111',state='market')
        self.assertEqual(result, 20)

    def test_all_symbols_market(self):
        result = get_score(game_result='X4/341412X513/1-X',state='market')
        self.assertEqual(result, 92)

    def test_all_symbols1_market(self):
        result = get_score(game_result='X4/-41-12X5-3/1--9',state='market')
        self.assertEqual(result, 79)

    def test_nines_market(self):
        with self.assertRaises(ValueError):
            get_score(game_result='99999999999999999999',state='market')

    def test_nine_market(self):
        with self.assertRaises(ValueError):
            get_score(game_result='X4/-41-79X5-3/1--9',state='market')

    def test_zero_result_market(self):
        result = get_score(game_result='--------------------',state='market')
        self.assertEqual(result, 0)

    def test_spare_market(self):
        result = get_score(game_result='1/1/1/1/1/1/1/1/1/1/',state='market')
        self.assertEqual(result, 109)

    def test_spare_first_market(self):
        with self.assertRaises(ValueError):
            get_score(game_result='/2/4/6/8/1/3/5/7/9/1',state='market')

    def test_all_numbers_market(self):
        result = get_score(game_result='2/4/6/8/1/3/5/7/9/1/',state='market')
        self.assertEqual(result, 144)

    def test_letters_market(self):
        with self.assertRaises(ValueError):
            get_score(game_result='qwerasdfzxcvtyghbnui',state='market')

    def test_frames_market(self):
        with self.assertRaises(Exception):
            get_score(game_result='2/4/6/8/1/3/5/7/9/1/X',state='market')

    def test_frames2_market(self):
        with self.assertRaises(Exception):
            get_score(game_result='2/4/6/8/1/3/5/7/9/1',state='market')

    def test_nothing_market(self):
        with self.assertRaises(Exception):
            get_score(game_result='',state='market')

    def test_zero_market(self):
        with self.assertRaises(Exception):
            get_score(game_result='0',state='market')


if __name__ == '__main__':
    unittest.main()


