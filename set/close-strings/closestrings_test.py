from closestrings import close_strings


def test_example_1():
    word1 = "abc"
    word2 = "bca"
    assert close_strings(word1, word2) == True


def test_example_2():
    word1 = "a"
    word2 = "aa"
    assert close_strings(word1, word2) == False


def test_example_3():
    word1 = "cabbba"
    word2 = "abbccc"
    assert close_strings(word1, word2) == True


def test_example_4():
    word1 = "cabbba"
    word2 = "aabbss"
    assert close_strings(word1, word2) == False


def test_example_5():
    word1 = "uau"
    word2 = "ssx"
    assert close_strings(word1, word2) == False
