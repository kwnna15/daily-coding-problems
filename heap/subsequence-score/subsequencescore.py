from heapq import heappush, heappop
from operator import itemgetter


class Solution:
    def max(self, nums1: list[int], nums2: list[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []

        for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            prefixSum += a
            heappush(minHeap, a)
            if len(minHeap) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(minHeap)
        return res
