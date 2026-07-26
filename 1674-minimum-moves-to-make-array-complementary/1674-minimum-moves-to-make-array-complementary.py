from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = n  # Start with maximum moves (change all)
        delta = [0] * (limit * 2 + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            mn, mx = min(a, b), max(a, b)
            # Update ranges: 2 moves [2,mn], 1 move [mn+1, a+b-1] and [a+b+1, mx+limit], 0 moves [a+b]
            delta[mn + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[mx + limit + 1] += 1
        
        # Compute prefix and find minimum moves
        moves = n
        for i in range(2, limit * 2 + 1):
            moves += delta[i]
            if moves < ans:
                ans = moves
        return ans