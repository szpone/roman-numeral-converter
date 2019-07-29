from unittest import main, TestCase
from roman_numeral_converter import roman_numeral_converter


class TestRomanNumeralConverter(TestCase):

    def test_convert_digit(self):
        value = roman_numeral_converter(5)

        self.assertEqual(value, "V")

    def test_convert_number(self):
        value = roman_numeral_converter(125)

        self.assertEqual(value, "CXXV")

    def test_convert_big_number(self):

        value = roman_numeral_converter(35289)

        self.assertEqual(value, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCCLXXXIX")


if __name__ == "__main__":
    main()