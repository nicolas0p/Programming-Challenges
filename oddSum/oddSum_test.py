import unittest
import oddSum as odd

class oddSumTest(unittest.TestCase):

    def test1(self):
        num = [-2, 2, -3, 1]
        result = odd.odd_sum(num)
        self.assertEqual(3, result)

    def test2(self):
        num = [2, -5, -3]
        #import pdb; pdb.set_trace()
        result = odd.odd_sum(num)
        self.assertEqual(-1, result)

    def test3(self):
        num = [-6004, 4882, 9052, 413, 6056, 4306, 9946, -4616, -6135, 906, -1718, 5252, -2866, 9061, 4046]
        result = odd.odd_sum(num)
        self.assertEqual(53507, result)

if __name__ == '__main__':
    unittest.main()
