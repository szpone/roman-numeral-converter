#!/usr/bin/env python3

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
    pass