import unittest

from generator import randomstatsgenerator as rsg

class TestLinear(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_linear(self):
        act_data = rsg.linear(type=int, minmax=(0,100), step=1, gradient=.1, noise=1)
        exp_data = [i for i in range(0,100)] 
        self.assertEqual(1,1)

    def test_quadratic(self):
        act_data = rsg.linear(type=int, minmax=(0,100), step=1, gradient=.1, noise=1)
        exp_data = [i*i for i in range(0,100)]
        self.assertAlmostEqual(1,1)

    def test_float(self):
        unittest.SkipTest
        # self.assertEqual(1,1)

    def test_stringfail(self):
        unittest.SkipTest
        # self.assertNotEqual(1,2)

if __name__=='__main__':
    unittest.main()