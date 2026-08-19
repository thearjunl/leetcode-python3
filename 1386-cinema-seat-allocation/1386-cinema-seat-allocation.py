from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(
        self,
        n: int,
        reservedSeats: List[List[int]]
    ) -> int:
        reserved = defaultdict(set)

        # Store only rows that contain reserved seats.
        for row, seat in reservedSeats:
            reserved[row].add(seat)

        # Every completely empty row can fit two families.
        answer = 2 * (n - len(reserved))

        for seats in reserved.values():
            left = all(seat not in seats for seat in range(2, 6))
            middle = all(seat not in seats for seat in range(4, 8))
            right = all(seat not in seats for seat in range(6, 10))

            if left and right:
                answer += 2
            elif left or middle or right:
                answer += 1

        return answer
        