"""
These unit tests will use smoke test, one-shot test and edge case test to
test the functionality of our recommend system including functions like:
recommend_k_movies_genre(), recommend_k_movies_year(),...

"""

import os, sys
sys.path.append("..")
from src.data_vis import *
from src.dash_vis import prepare_data
import unittest



class UnitTests(unittest.TestCase):

    # smoke test 1
    # test recommend_k_movies_genre()
    def test1(self):
        data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        df = prepare_data(data_path)
        res = recommend_k_movies_genre(df, 'action', 10)
        # print(res)

    # smoke test 2
    # test recommend_k_movies_year()
    def test2(self):
        data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        df = prepare_data(data_path)
        res = recommend_k_movies_year(df, 2009, 10)
        # print(res)



    # edge case test 1
    # test recommend_k_movies_year()
    def test3(self):
        # edge tests -- if the size of result (size) smaller than k, k = size
        data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        df = prepare_data(data_path)
        # our dataset only have one movie in 2017
        res = recommend_k_movies_year(df, 2017, 10)
        self.assertEqual(len(res), 1)



    # edge case test 2
    # test recommend_k_movies_genre()
    def test4(self):
        # edge tests -- if the size of result (size) smaller than k, k = size
        data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        df = prepare_data(data_path)
        # our dataset only have 34 'foreign' movies
        res = recommend_k_movies_genre(df, 'foreign', 50)
        self.assertEqual(len(res), 34)


    # edge case test 3
    # test recommend_k_movies_genre()
    def test5(self):
        # edge tests -- if the dataframe is empty or None
        with self.assertRaises(ValueError):
            df = {}
            recommend_k_movies_genre(df, 'action', 10)


    # edge case test 4
    # test recommend_k_movies_year()
    def test6(self):
        # edge tests -- if the dataframe is empty or None
        with self.assertRaises(ValueError):
            df = {}
            recommend_k_movies_year(df, 'action', 10)

    # edge case test 5
    # test recommend_k_movies_genre()
    def test7(self):
        # edge tests -- if the genre type is not string
        with self.assertRaises(ValueError):
            data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
            df = prepare_data(data_path)
            recommend_k_movies_genre(df, 111, 10)


    # edge case test 6
    # test recommend_k_movies_year()
    def test8(self):
        # edge tests -- if the year type is not integer
        with self.assertRaises(ValueError):
            data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
            df = prepare_data(data_path)
            recommend_k_movies_year(df, '2011', 10)


    # one-shot test 1
    # test recommend_k_movies_genre()
    def test9(self):
        data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        df = prepare_data(data_path)
        res = recommend_k_movies_genre(df, 'action', 5)
        ans = {'The Lord of the Rings: The Return of the King': 8.1, 'The Dark Knight': 8.2, \
                'The Empire Strikes Back': 8.2, '七人の侍': 8.2, "One Man's Hero": 9.3}
        self.assertEqual(res, ans)


    # one-shot test 2
    # test recommend_k_movies_year()
    def test10(self):
        data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        df = prepare_data(data_path)
        res = recommend_k_movies_year(df, 2017, 5)
        ans = [('Growing Up Smith', 7.4)]
        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()
