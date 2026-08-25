from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = set()

        for x in nums:
            if x % k == 0:
                present.add(x // k)

        m = 1
        while m in present:
            m += 1

        return m * k