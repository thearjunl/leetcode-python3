from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from index i onward
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i: int, m: int) -> int:
            # Current player can take all remaining piles
            if i + 2 * m >= n:
                return suffix[i]

            best = 0

            # Take x piles, where 1 <= x <= 2 * m
            for x in range(1, 2 * m + 1):
                opponent = dfs(i + x, max(m, x))
                current = suffix[i] - opponent
                best = max(best, current)

            return best

        return dfs(0, 1)