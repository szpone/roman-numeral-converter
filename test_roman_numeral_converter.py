from unittest import main, TestCase
from roman_numeral_converter import roman_numeral_converter


class TestRomanNumeralConverter(TestCase):

    def test_convert_digit(self):
        value = roman_numeral_converter(5)

        self.assertEqual(value, "V")

    def test_convert_number(self):
        value = roman_numeral_converter(125)

        self.assertEqual(value, "CXXV")


    def test_number_zero(self):
        value = roman_numeral_converter(0)

        self.assertEqual(value, "Error! Number is zero")


if __name__ == "__main__":
    main()
