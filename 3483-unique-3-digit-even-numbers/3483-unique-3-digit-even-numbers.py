from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        n = len(digits)

        for i in range(n):          # hundreds place
            if digits[i] == 0:
                continue
            for j in range(n):      # tens place
                if j == i:
                    continue
                for k in range(n):  # units place
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    seen.add(num)

        return len(seen)