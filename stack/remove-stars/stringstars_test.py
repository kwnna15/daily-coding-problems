from stringstars import remove


def test_example_1():
    s = "leet**cod*e"
    assert remove(s) == "lecoe"


def test_example_2():
    s = "erase*****"
    assert remove(s) == ""


def test_example_3():
    s = "ab**c*d*e"
    assert remove(s) == "e"


def test_example_4():
    s = "a*b*c*d*e*"
    assert remove(s) == ""


def test_example_5():
    s = "abc*de*f*gh*"
    assert remove(s) == "abdg"
