from maxvowels import max_vowels

def test_example_1():
    s = "abciiidef"
    k = 3
    assert max_vowels(s, k) == 3

def test_example_2():
    s = "aeiou"
    k = 2
    assert max_vowels(s, k) == 2

def test_example_3():
    s = "leetcode"
    k = 3
    assert max_vowels(s, k) == 2

def test_example_4():
    s = "rhythms"
    k = 4
    assert max_vowels(s, k) == 0

def test_example_5():
    s = "tryhard"
    k = 4
    assert max_vowels(s, k) == 1