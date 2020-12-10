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
    
    # edge case test 2
    # test recommend_k_movies_genre()
    def test5(self):
        # edge tests -- if the dataframe is empty or None
        with self.assertRaises(ValueError):
            df = {}
            recommend_k_movies_genre(df, 'action', 10)


    """
    # one-shot test 1 
    def test_success5(self):
        print("one-shot test 1")
        # data = [[1, 1, 135], 
        #         [2, 5, 433],
        #         [3, 2, 319],
        #         [4, 4, 252],
        #         [5, 5, 421],
        #         [2, 4, 214],
        #         [3, 6, 501]] 
        # query = [1, 3]
        # k = 3
        # ans should be 222.67
        data5 = [[1, 1, 135], [2, 5, 433], [3, 2, 319], [4, 4, 252], [5, 5, 421], [2, 4, 214], [3, 6, 501]]
        mean5 = knn_regression(3, data5, [1, 3])
        print(mean5)
        self.assertEqual(mean5, 222.67)
        

    # one-shot test 2
    def test_success6(self):
        print("one-shot test 2")
        # data = [[1, 1, 135], 
        #         [2, 5, 433],
        #         [3, 2, 319],
        #         [4, 4, 252],
        #         [5, 5, 421],
        #         [2, 4, 214],
        #         [3, 6, 501]] 
        # query = [7, 8]
        # k = 2
        # ans should be 391.33
        data6 = [[1, 1, 135], [2, 5, 433], [3, 2, 319], [4, 4, 252], [5, 5, 421], [2, 4, 214], [3, 6, 501]]
        mean6 = knn_regression(3, data6, [7, 8])
        print(mean6)
        self.assertEqual(mean6, 391.33)

    """

if __name__ == '__main__':
    unittest.main()
