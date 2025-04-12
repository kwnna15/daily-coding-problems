class Solution:
    def count(self, n: int) -> list[int]:
        counter = [0]
        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
