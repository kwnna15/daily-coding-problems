from guessnum import Solution


def mock_guess(pick):
    def guess(num):
        if num < pick:
            return 1
        elif num > pick:
            return -1
        else:
            return 0

    return guess


def test_example_1(monkeypatch):
    pick = 6
    solution = Solution()
    monkeypatch.setattr(solution, "guess", mock_guess(pick))
    assert solution.guessnum(10) == 6


def test_example_2(monkeypatch):
    pick = 1
    solution = Solution()
    monkeypatch.setattr(solution, "guess", mock_guess(pick))
    assert solution.guessnum(1) == 1


def test_example_3(monkeypatch):
    pick = 500
    solution = Solution()
    monkeypatch.setattr(solution, "guess", mock_guess(pick))
    assert solution.guessnum(1000) == 500


def test_example_4(monkeypatch):
    pick = 10
    solution = Solution()
    monkeypatch.setattr(solution, "guess", mock_guess(pick))
    assert solution.guessnum(20) == 10


def test_example_5(monkeypatch):
    pick = 100
    solution = Solution()
    monkeypatch.setattr(solution, "guess", mock_guess(pick))
    assert solution.guessnum(200) == 100
