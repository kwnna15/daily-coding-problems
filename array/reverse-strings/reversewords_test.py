from reversewords import reverse_words


def test_example_1():
    s = "the sky is blue"
    assert reverse_words(s) == "blue is sky the"


def test_example_2():
    s = "  hello world  "
    assert reverse_words(s) == "world hello"


def test_example_3():
    s = "a good   example"
    assert reverse_words(s) == "example good a"


def test_example_4():
    s = "  Bob    Loves  Alice   "
    assert reverse_words(s) == "Alice Loves Bob"


def test_example_5():
    s = "Alice does not even like bob"
    assert reverse_words(s) == "bob like even not does Alice"
