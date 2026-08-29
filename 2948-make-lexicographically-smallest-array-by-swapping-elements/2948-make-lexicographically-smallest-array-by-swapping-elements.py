from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Pair each value with its original index and sort by value.
        sorted_with_indices = sorted(zip(nums, range(n)))

        result = [0] * n
        i = 0

        while i < n:
            # Extend the current group while consecutive values differ by at most limit.
            j = i + 1
            while j < n and sorted_with_indices[j][0] - sorted_with_indices[j - 1][0] <= limit:
                j += 1

            # Original indices in this group.
            original_indices = sorted(idx for _, idx in sorted_with_indices[i:j])

            # Place the smallest values at the smallest original positions.
            for pos, (val, _) in zip(original_indices, sorted_with_indices[i:j]):
                result[pos] = val

            i = j

        return result