from typing import List
from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = Counter(stone % 3 for stone in stones)

        # If the number of remainder-0 stones is even
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0

        # If the number of remainder-0 stones is odd
        return abs(count[1] - count[2]) > 2