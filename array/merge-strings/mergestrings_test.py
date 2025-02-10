from mergestrings import merge_strings


def test_example_1():
    word1 = "abc"
    word2 = "pqr"
    assert merge_strings(word1, word2) == "apbqcr"


def test_example_2():
    word1 = "ab"
    word2 = "pqrs"
    assert merge_strings(word1, word2) == "apbqrs"


def test_example_3():
    word1 = "abcd"
    word2 = "pq"
    assert merge_strings(word1, word2) == "apbqcd"


def test_example_4():
    word1 = ""
    word2 = "xyz"
    assert merge_strings(word1, word2) == "xyz"


def test_example_5():
    word1 = "hello"
    word2 = ""
    assert merge_strings(word1, word2) == "hello"
