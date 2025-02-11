import sys
from math import gcd


def max_candies(candies: list[int], extra_candies: int) -> list[bool]:
    max_candies = max(candies)
    return [(candy + extra_candies) >= max_candies for candy in candies]
