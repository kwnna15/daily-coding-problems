import sys


def sum_to_k(list, k):
    visited = {}
    for i in list:
        val = visited.get(k - i)
        if visited.get(k - i) != None:
            return [i, val]
        else:
            visited[i] = i


if __name__ == "__main__":
    list = numbers = [int(num) for num in sys.argv[1].split(",")]
    k = int(sys.argv[2])
    print(sum_to_k(list, k))
