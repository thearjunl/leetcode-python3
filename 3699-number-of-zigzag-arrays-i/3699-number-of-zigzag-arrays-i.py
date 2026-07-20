from typing import List

MOD = 10**9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m % MOD

        up = [0] * m
        down = [0] * m
        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            pref = 0
            for i in range(m):
                new_up[i] = pref
                pref = (pref + down[i]) % MOD

            pref = 0
            for i in range(m - 1, -1, -1):
                new_down[i] = pref
                pref = (pref + up[i]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD