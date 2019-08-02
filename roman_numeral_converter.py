#!/usr/bin/env python

from typing import Dict


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

    while number > 0:
        for key, value in  ROMAN_NUMERALS.items():
            quotient, remainder = divmod(number, value)
            print(quotient, remainder)

            if quotient is not 0:
                result.append(quotient * key)
                number = remainder


    return "".join(result)


roman_numeral_converter(1997)

