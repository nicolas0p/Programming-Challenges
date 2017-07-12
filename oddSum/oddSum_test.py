import unittest
import oddSum as odd

class oddSumTest(unittest.TestCase):

    def test1(self):
        num = [-2, 2, -3, 1]
        #import pdb; pdb.set_trace()
        result = odd.odd_sum(num)
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()
