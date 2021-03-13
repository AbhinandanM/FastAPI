import unittest
from modules.maths import Factorial, Fibonacci

# A test class for maths.py


class TestMaths(unittest.TestCase):
    def test_Fibonacci(self):
        """
        Test the Function Fibonacci from maths.py
        """
        data = 9
        result = Fibonacci(data)
        self.assertEqual(result, {'9th Fibonacci number is': 34})

    def test_Factorial(self):
        '''
        Test the Function Factorial from maths.py
        '''
        data = 3
        result = Factorial(data)
        self.assertEqual(result, {'The factorial of 3 is': 6})


if __name__ == '__main__':
    unittest.main()
