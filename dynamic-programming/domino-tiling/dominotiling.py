class Solution:
    def tilings(self, n: int) -> int:
        full = {0: 1, 1: 1}
        top = {1: 0}
        bottom = {1: 0}

        for i in range(2, n + 1):
            full[i] = full[i - 1] + full[i - 2] + top[i - 1] + bottom[i - 1]
            top[i] = full[i - 2] + bottom[i - 1]
            bottom[i] = full[i - 2] + top[i - 1]

        return full[n] % (10**9 + 7)
