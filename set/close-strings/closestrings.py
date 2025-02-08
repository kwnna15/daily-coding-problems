import sys
from collections import Counter


def close_strings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False

    f1 = Counter(word1)
    f2 = Counter(word2)

    if sorted(f1.values()) != sorted(f2.values()):
        return False

    return True


if __name__ == "__main__":
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    print(close_strings(word1, word2))
