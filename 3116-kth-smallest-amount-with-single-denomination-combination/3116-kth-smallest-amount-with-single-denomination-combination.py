from typing import List
from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        m = len(coins)

        def count(limit: int) -> int:
            """
            Count positive amounts <= limit that are divisible
            by at least one denomination.
            """
            total = 0

            # Inclusion-exclusion over all non-empty subsets.
            for mask in range(1, 1 << m):
                lcm = 1
                bits = 0
                valid = True

                for i in range(m):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm // gcd(lcm, coins[i]) * coins[i]

                        if lcm > limit:
                            valid = False
                            break

                if valid:
                    multiples = limit // lcm

                    if bits % 2 == 1:
                        total += multiples
                    else:
                        total -= multiples

            return total

        low = 1
        high = min(coins) * k

        # Binary search for the smallest amount having at least k valid amounts.
        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low