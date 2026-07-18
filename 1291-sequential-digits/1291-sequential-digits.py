from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []

        low_len = len(str(low))
        high_len = len(str(high))

        # Try all possible lengths between low_len and high_len
        for length in range(low_len, high_len + 1):
            # Slide a window of size `length` over "123456789"
            for start in range(0, 10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    res.append(num)

        return res
        