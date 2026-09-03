from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        # If all numbers have the same parity, we can keep them as-is.
        all_even = all(x % 2 == 0 for x in nums1)
        all_odd = all(x % 2 == 1 for x in nums1)

        if all_even or all_odd:
            return True

        # There are both even and odd numbers.
        # To make all elements odd, we need the smallest odd number.
        min_odd = min(x for x in nums1 if x % 2 == 1)

        # For every even number x, we must have x - min_odd >= 1.
        for x in nums1:
            if x % 2 == 0 and x - min_odd < 1:
                return False

        return True