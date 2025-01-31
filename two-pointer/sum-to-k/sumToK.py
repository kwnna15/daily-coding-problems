import sys


def sumToK(list, k):
    seen = {}
    for i in list:
        seenValue = seen.get(k - i)
        if seen.get(k - i) != None:
            return [i, seenValue]
        else:
            seen[i] = i


if __name__ == "__main__":
    list = numbers = [int(num) for num in sys.argv[1].split(",")]
    k = int(sys.argv[2])
    print(sumToK(list, k))
