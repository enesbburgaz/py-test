import unittest
import calc


class TestCalcMethods(unittest.TestCase):
    """
    docstring
    """
    def test_add(self):
        """
        docstring
        """
        self.assertEqual(calc.add(3,5), 8)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5,3),2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3,3),9)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,2),5)

if __name__ == '__main__':
    unittest.main( )