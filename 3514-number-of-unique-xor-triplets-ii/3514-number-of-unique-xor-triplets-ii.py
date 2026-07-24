from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = set(nums)
        pair_xor = set()

        for a in vals:
            for b in vals:
                pair_xor.add(a ^ b)

        triplet_xor = set()
        for p in pair_xor:
            for c in vals:
                triplet_xor.add(p ^ c)

        return len(triplet_xor)