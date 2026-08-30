from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        # Find positions of minimum and maximum elements.
        min_idx = 0
        max_idx = 0

        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Option 1: delete both from the front.
        option1 = right + 1

        # Option 2: delete both from the back.
        option2 = n - left

        # Option 3: delete one from the front and the other from the back.
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)