from subsequence import is_subsequence

def test_example_1():
    s = "abc"
    t = "ahbgdc"
    assert is_subsequence(s, t) == True

def test_example_2():
    s = "axc"
    t = "ahbgdc"
    assert is_subsequence(s, t) == False

def test_example_3():
    s = ""
    t = "ahbgdc"
    assert is_subsequence(s, t) == True

def test_example_4():
    s = "abc"
    t = ""
    assert is_subsequence(s, t) == False

def test_example_5():
    s = "ace"
    t = "abcde"
    assert is_subsequence(s, t) == True