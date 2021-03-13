import unittest
from modules.strings import generateStr, lenOfStr

# A test class for strings.py


class TestStrings(unittest.TestCase):
    def test_generateStr(self):
        """
        Test the Function generateStr from strings.py
        """
        char = "t"
        data = 5
        result = generateStr(char=char, count=data)
        self.assertEqual(result, {"String": 'ttttt'})

    def test_lenOFStr(self):
        '''
        Test the Function lenOfStr from strings.py
        '''
        char = 'testdata'
        result = lenOfStr(string=char)
        self.assertEqual(result, {"String length": 8})


if __name__ == '__main__':
    unittest.main()
