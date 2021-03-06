import unittest
from modules.strings import generate_string, len_of_string

# A test class for strings.py


class TestStrings(unittest.TestCase):
    def test_generateStr(self):
        """
        Test the Function generate_string from strings.py
        """
        char = "t"
        data = 5
        result = generate_string(char=char, count=data)
        self.assertEqual(result, {"String": 'ttttt'})

    def test_lenOFStr(self):
        '''
        Test the Function len_of_string from strings.py
        '''
        char = 'testdata'
        result = len_of_string(string=char)
        self.assertEqual(result, {"String length": 8})


if __name__ == '__main__':
    unittest.main()
