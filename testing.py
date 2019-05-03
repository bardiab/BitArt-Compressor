import unittest
from compress import *

class MyTests(unittest.TestCase):

    def test_isNum(self):
        """
        Test that a string is correclty identified as a number
        """
        data = '4'
        result = obj.is_number(data)
        self.assertEqual(result, True)

        data2 = '@'
        result2 = obj.is_number(data2)
        self.assertEqual(result2, False)


    def test_compressString(self):
        """
        Test that a string is correctly compressed
        """
        #Test with newline character
        string = ",+@+,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:'@@#@#',,,,,,+@+,\n"
        result = obj.compress_string(string)
        self.assertEqual(result, ",+@+,32:'@2#@#',6+@+,")

        #Test without newline character
        string2 = ",#@',,,,,,,,,,,,,,,,,,,+@##@@;,,,,,,,,,,,,,,,,,,,,,,+@+"
        result2 = obj.compress_string(string2)
        self.assertEqual(result2, ",#@',19+@#2@2;,22+@+")


    def test_decompString(self):
        """
        Test that a string is correclty decompressed
        """

        #Basic test
        string = ",#@4+,"
        result = obj.decompress_string(string)
        self.assertEqual(result, ",#@@@@+,")

        #Test if decompress works with double digit repeated characters
        string2 = ",+@+,32:'@2#@#',6+@+,"
        result2 = obj.decompress_string(string2)
        self.assertEqual(result2, ",+@+,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:'@@#@#',,,,,,+@+,")

        #Testing for index out of bounds errors
        string3 = ",2"
        result3 = obj.decompress_string(string3)
        self.assertEqual(result3, ",,")


    def test_repeated(self):
        """
        Tests to ensure the correct number of times a character is reapeated
        """
        string = ",+@+,28+@2,25+@+,"
        result = obj.get_repeated(string)
        self.assertEqual(result, '28')

        string2 = "32+@+,"
        result2 = obj.get_repeated(string2)
        self.assertEqual(result2, '32')

# Main Function
if __name__ == '__main__':
    obj = Compression()
    unittest.main()
