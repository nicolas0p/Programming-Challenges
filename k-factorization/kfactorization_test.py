import unittest
import kfactorization as k

class kFactorizationTest(unittest.TestCase):

    def test1(self):
        num = 100000
        qtd = 2
        #import pdb; pdb.set_trace()
        result = k.kfactorization(num, qtd)
        self.assertCountEqual([2, 50000], result)

    def test2(self):
        num = 100000
        qtd = 20
        result = k.kfactorization(num, qtd)
        self.assertCountEqual([-1], result)

    def test3(self):
        num = 1024
        qtd = 5
        result = k.kfactorization(num, qtd)
        self.assertCountEqual([2, 64, 2, 2, 2], result)

    def test4(self):
        num = 1024
        qtd = 11
        result = k.kfactorization(num, qtd)
        self.assertCountEqual([-1], result)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
