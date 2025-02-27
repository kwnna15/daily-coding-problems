from decodestring import decode


def test_example_1():
    s = "3[a]2[bc]"
    assert decode(s) == "aaabcbc"


def test_example_2():
    s = "3[a2[c]]"
    assert decode(s) == "accaccacc"


def test_example_3():
    s = "2[abc]3[cd]ef"
    assert decode(s) == "abcabccdcdcdef"


def test_example_4():
    s = "10[a]"
    assert decode(s) == "aaaaaaaaaa"


def test_example_5():
    s = "2[3[a]b]"
    assert decode(s) == "aaabaaab"
