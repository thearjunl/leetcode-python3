from typing import List
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def dfs(i: int) -> int:
            # Maximum (current player score - opponent score) from position i
            if i >= n:
                return 0
            best = float("-inf")
            s = 0
            for k in range(1, 4):  # take 1, 2, or 3 stones
                if i + k > n:
                    break
                s += stoneValue[i + k - 1]
                best = max(best, s - dfs(i + k))
            return best

        diff = dfs(0)  # Alice's score - Bob's score when both play optimally
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"