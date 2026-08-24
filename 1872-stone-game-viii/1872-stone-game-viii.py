from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sum of all stones.
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # With two stones remaining, the current player must take both.
        best = prefix[-1]

        # Try possible prefix lengths from right to left.
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)

        return best