import heapq


class Solution:
    def calculate(self, costs: list[int], k: int, candidates: int) -> int:
        lheap = costs[:candidates]
        rheap = costs[max(candidates, len(costs) - candidates) :]
        heapq.heapify(lheap)
        heapq.heapify(rheap)
        l, r = candidates, len(costs) - candidates - 1
        total_cost = 0

        while k > 0:
            if rheap and (not lheap or rheap[0] < lheap[0]):
                total_cost += heapq.heappop(rheap)
                if l <= r:
                    heapq.heappush(rheap, costs[r])
                    r -= 1
            else:
                total_cost += heapq.heappop(lheap)
                if l <= r:
                    heapq.heappush(lheap, costs[l])
                    l += 1
            k -= 1

        return total_cost
