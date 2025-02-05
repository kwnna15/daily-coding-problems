import sys


def unique_occurrences(arr: list[int]) -> bool:
    occurrences = {}
    for k in arr:
        occurrences[k] = occurrences.get(k, 0) + 1

    return len(set(occurrences.values())) == len(occurrences)


if __name__ == "__main__":
    arr = list(map(int, sys.argv[1].split(",")))
    print(unique_occurrences(arr))
