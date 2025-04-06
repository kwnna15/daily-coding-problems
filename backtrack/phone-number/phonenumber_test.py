from phonenumber import Solution


def test_example_1():
    digits = "23"
    sol = Solution()
    assert sorted(sol.combinations(digits)) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )


def test_example_2():
    digits = ""
    sol = Solution()
    assert sol.combinations(digits) == []


def test_example_3():
    digits = "2"
    sol = Solution()
    assert sorted(sol.combinations(digits)) == sorted(["a", "b", "c"])


def test_example_4():
    digits = "7"
    sol = Solution()
    assert sorted(sol.combinations(digits)) == sorted(["p", "q", "r", "s"])


def test_example_5():
    digits = "79"
    sol = Solution()
    assert sorted(sol.combinations(digits)) == sorted(
        [
            "pw",
            "px",
            "py",
            "pz",
            "qw",
            "qx",
            "qy",
            "qz",
            "rw",
            "rx",
            "ry",
            "rz",
            "sw",
            "sx",
            "sy",
            "sz",
        ]
    )
