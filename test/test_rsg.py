import unittest

from generator import randomstatsgenerator as rsg

class TestLinear(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_integer(self):
        self.assertEqual(1,1)

    def test_double(self):
        self.assertEqual(1,1)

    def test_float(self):
        self.assertEqual(1,1)

    def test_stringfail(self):
        self.assertNotEqual(1,2)

if __name__=='__main__':
    unittest.main()