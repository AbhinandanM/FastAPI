import unittest
from modules.maths import return_fibonacci_num, return_factorial_of_num

# A test class for maths.py


class TestMaths(unittest.TestCase):
    def test_Fibonacci(self):
        """
        Test the Function return_fibonacci_num from maths.py
        """
        data = 9
        result = return_fibonacci_num(data)
        self.assertEqual(result, {'9th Fibonacci number is': 34})

    def test_Factorial(self):
        '''
        Test the Function return_factorial_of_num from maths.py
        '''
        data = 3
        result = return_factorial_of_num(data)
        self.assertEqual(result, {'The factorial of 3 is': 6})


if __name__ == '__main__':
    unittest.main()
