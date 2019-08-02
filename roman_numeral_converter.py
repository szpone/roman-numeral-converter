#!/usr/bin/env python

from sys import argv
from typing import Dict
import argparse


ROMAN_NUMERALS: Dict[str, int] = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}


def roman_numeral_converter(number: int) -> str:
    result = []

    if number == 0:
        return "Error! Number is zero"

    while int(number) > 0:
        for key, value in  ROMAN_NUMERALS.items():
            quotient, remainder = divmod(number, value)

            if quotient is not 0:
                result.append(quotient * key)
                number = remainder

    return "".join(result)


parser = argparse.ArgumentParser()
parser.add_argument("number", default="check_string_for_empty", help="Argument should be an int", type=int)
args = parser.parse_args()


roman_numeral_converter(int(argv[1]))

