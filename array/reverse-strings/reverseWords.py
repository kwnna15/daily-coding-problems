import sys
from math import gcd


def reverseWords(s: str) -> str:
    word = ""
    reverse = ""
    for i in range(0, len(s)):
        c = s[i]
        if i == len(s) - 1:
            if c != " ":
                word += c
            if len(reverse) == 0 and len(word) > 0:
                reverse = word
            elif len(word) == 0:
                continue
            else:
                reverse = word + " " + reverse
        elif c != " ":
            word += c
            continue
        elif len(reverse) == 0:
            reverse = word
        elif len(word) > 0:
            reverse = word + " " + reverse
        word = ""

    return reverse


if __name__ == "__main__":
    s = sys.argv[1]
    print(reverseWords(s))
