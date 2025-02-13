from reversevowels import reverse_vowels

def test_example_1():
    s = "hello"
    assert reverse_vowels(s) == "holle"

def test_example_2():
    s = "leetcode"
    assert reverse_vowels(s) == "leotcede"

def test_example_3():
    s = "aA"
    assert reverse_vowels(s) == "Aa"

def test_example_4():
    s = "aeiou"
    assert reverse_vowels(s) == "uoiea"

def test_example_5():
    s = "bcdfg"
    assert reverse_vowels(s) == "bcdfg"