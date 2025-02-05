import pytest
from gcdstrings import gcd_strings


def test_example_1():
    str1 = "ABCABC"
    str2 = "ABC"
    assert gcd_strings(str1, str2) == "ABC"


def test_example_2():
    str1 = "ABABAB"
    str2 = "ABAB"
    assert gcd_strings(str1, str2) == "AB"


def test_example_3():
    str1 = "LEET"
    str2 = "CODE"
    assert gcd_strings(str1, str2) == ""


def test_example_4():
    str1 = "AAAA"
    str2 = "AA"
    assert gcd_strings(str1, str2) == "AA"


def test_example_5():
    str1 = "ABCDEF"
    str2 = "ABC"
    assert gcd_strings(str1, str2) == ""
