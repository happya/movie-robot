"""
These unit tests will use smoke test, one-shot test and edge case test to
test the functionality of our recommend system including functions like:
recommend_k_movies_genre(), recommend_k_movies_year(),...

"""

import os, sys
import pandas as pd

sys.path.append("..")
from src.data_vis import *
from src.dash_vis import prepare_data
import unittest


class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data_path = os.path.abspath(os.path.join(__file__, '../../data/movies_cleaned.csv'))
        self.df = prepare_data(self.data_path)
        self.empty_df = pd.DataFrame()

    # smoke test 1
    # test recommend_k_movies_genre()
    def test_valid_recommend_movies_genre(self):
        recommend_k_movies_genre(self.df, 'action', 10)

    # smoke test 2
    # test recommend_k_movies_year()
    def test_valid_recommend_movies_year(self):
        recommend_k_movies_year(self.df, 2009, 10)

    # edge case test 1
    # test recommend_k_movies_year()
    def test_recommend_year_result(self):
        # edge tests -- if the size of result (size) smaller than k, k = size
        # our dataset only have one movie in 2017
        res = recommend_k_movies_year(self.df, 2017, 10)
        self.assertEqual(len(res), 1)

    # edge case test 2
    # test recommend_k_movies_genre()
    def test_recommend_size_smaller_than_k(self):
        # edge tests -- if the size of result (size) smaller than k, k = size
        # our dataset only have 34 'foreign' movies
        res = recommend_k_movies_genre(self.df, 'foreign', 50)
        self.assertEqual(len(res), 34)

    # edge case test 3
    # test recommend_k_movies_genre()
    def test_recommend_genre_empty_df(self):
        # edge tests -- if the dataframe is empty or None
        with self.assertRaises(ValueError):
            recommend_k_movies_genre(self.empty_df, 'action', 10)

    # edge case test 4
    # test recommend_k_movies_year()
    def test_recommend_year_empty_df(self):
        # edge tests -- if the dataframe is empty or None
        with self.assertRaises(ValueError):
            recommend_k_movies_year(self.empty_df, 'action', 10)

    # edge case test 5
    # test recommend_k_movies_genre()
    def test_invalid_genre(self):
        # edge tests -- if the genre type is not string
        with self.assertRaises(TypeError):
            recommend_k_movies_genre(self.df, 111, 10)

    # one-shot test 1
    # test recommend_k_movies_genre()
    def test_recommend_movies_genre(self):
        res = recommend_k_movies_genre(self.df, 'action', 5)
        ans = {'The Lord of the Rings: The Return of the King': 8.1, 'The Dark Knight': 8.2, \
               'The Empire Strikes Back': 8.2, '七人の侍': 8.2, "One Man's Hero": 9.3}
        self.assertEqual(res, ans)

    # one-shot test 2
    # test recommend_k_movies_year()
    def test_recommend_movies_year(self):
        res = recommend_k_movies_year(self.df, 2017, 5)
        ans = [('Growing Up Smith', 7.4)]
        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()
