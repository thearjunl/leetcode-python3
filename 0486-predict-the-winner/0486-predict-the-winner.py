from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            # Maximum score difference (current player - opponent)
            # for the subarray nums[i..j]
            if i > j:
                return 0
            # Pick left or right; opponent will play optimally next
            return max(nums[i] - dfs(i + 1, j),
                       nums[j] - dfs(i, j - 1))

        # If Player 1 can achieve a non-negative score difference, they can win/tie
        return dfs(0, n - 1) >= 0