import unittest
import kfactorization as k

class kFactorizationTest(unittest.TestCase):

    def test1(self):
        num = 100000
        qtd = 2
        #import pdb; pdb.set_trace()
        result = k.kfactorization(num, qtd)
        self.assertListEqual([2, 50000], result)

    def test2(self):
        num = 100000
        qtd = 20
        result = k.kfactorization(num, qtd)
        self.assertListEqual([-1], result)

if __name__ == '__main__':
    unittest.main()
