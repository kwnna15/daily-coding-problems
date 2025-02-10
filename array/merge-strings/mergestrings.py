import sys
from math import gcd


def merge_strings(str1: str, str2: str) -> str:
    out = []
    for i, j in zip(str1, str2):
        out.append(i)
        out.append(j)

    out.append(str1[len(str2) :])
    out.append(str2[len(str1) :])

    return "".join(out)


if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(merge_strings(str1, str2))
