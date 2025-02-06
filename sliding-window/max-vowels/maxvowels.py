import sys


def max_vowels(s: str, k: int) -> int:
    n = len(s)
    vowels = {"a", "e", "i", "o", "u"}
    count = sum(1 for i in s[:k] if i in vowels)
    max_count = count
    for i in range(n - k):
        if s[i] in vowels:
            count -= 1
        if s[i + k] in vowels:
            count += 1
        max_count = max(count, max_count)
    return max_count


if __name__ == "__main__":
    s = k = sys.argv[1]
    k = int(sys.argv[2])
    print(max_vowels(s, k))
