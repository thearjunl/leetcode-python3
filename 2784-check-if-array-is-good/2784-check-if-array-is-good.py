from collections import Counter
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        count = Counter(nums)
        
        for x in range(1, n):
            if count[x] != 1:
                return False
        
        return count[n] == 2