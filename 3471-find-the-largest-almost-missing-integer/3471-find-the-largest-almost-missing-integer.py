from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequency = {}

        # Count how many subarrays of length k contain each value.
        for start in range(n - k + 1):
            seen = set(nums[start:start + k])

            for value in seen:
                frequency[value] = frequency.get(value, 0) + 1

        # An almost missing integer appears in exactly one subarray.
        answer = -1

        for value, count in frequency.items():
            if count == 1:
                answer = max(answer, value)

        return answer