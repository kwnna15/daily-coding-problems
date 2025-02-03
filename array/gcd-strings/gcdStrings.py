import sys
from math import gcd


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    lenGcd = gcd(len(str1), len(str2))
    return str1[:lenGcd]


if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(gcdOfStrings(str1, str2))
