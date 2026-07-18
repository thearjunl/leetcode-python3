from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        num_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            num_to_indices[num].append(i)
        
        for indices in num_to_indices.values():
            n = len(indices)
            if n == 1:
                continue
            sum_so_far = sum(indices)
            prev_index = 0
            for i in range(n):
                sum_so_far += (i - 1) * (indices[i] - prev_index)
                sum_so_far -= (n - 1 - i) * (indices[i] - prev_index)
                ans[indices[i]] = sum_so_far
                prev_index = indices[i]
        return ans
        