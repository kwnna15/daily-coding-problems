import math
from bisect import bisect_left


class Solution:
    def calculate(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        num_potions = len(potions)
        potions.sort()
        pairs = []
        for spell in spells:
            candidate = math.ceil(success / spell)
            idx = bisect_left(potions, candidate)
            pairs.append(num_potions - idx)
        return pairs
