import unittest
import les29

class TestPlusFunction(unittest.TestCase):
    def test_plus(self): 
        test_num = 10
        result = les29.plus(test_num)
        self.assertEqual(result, 15)
    def test_plus_not_equal(self): 
        test_num = 10
        result = les29.plus(test_num)
        self.assertEqual(result, 10)

    def test_plus_passing_string(self): 
        test_num = 'a'
        result = les29.plus(test_num)
        self.assertIsInstance(result, ValueError)


unittest.main()
