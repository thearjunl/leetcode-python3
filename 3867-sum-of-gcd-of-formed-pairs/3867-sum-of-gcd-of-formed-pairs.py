from typing import List
from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        arr = []
        cur_max = 0

        for x in nums:
            cur_max = max(cur_max, x)
            arr.append(gcd(x, cur_max))

        arr.sort()

        left, right = 0, len(arr) - 1
        ans = 0

        while left < right:
            ans += gcd(arr[left], arr[right])
            left += 1
            right -= 1

        return ans