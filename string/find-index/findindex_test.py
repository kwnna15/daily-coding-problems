from findindex import Solution


def test_example_1():
    haystack = "sadbutsad"
    needle = "sad"
    sol = Solution()
    assert sol.find(haystack, needle) == 0


def test_example_2():
    haystack = "leetcode"
    needle = "leeto"
    sol = Solution()
    assert sol.find(haystack, needle) == -1


def test_example_3():
    haystack = "hello"
    needle = "ll"
    sol = Solution()
    assert sol.find(haystack, needle) == 2


def test_example_4():
    haystack = "aaaaa"
    needle = "bba"
    sol = Solution()
    assert sol.find(haystack, needle) == -1


def test_example_5():
    haystack = "abc"
    needle = ""
    sol = Solution()
    assert sol.find(haystack, needle) == 0
