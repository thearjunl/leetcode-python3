from typing import List
from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = Counter(nums)

        # cnt_g[i] = number of pairs whose gcd is exactly i
        cnt_g = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            v = 0
            for j in range(i, mx + 1, i):
                v += cnt[j]
            cnt_g[i] = v * (v - 1) // 2
            for j in range(i * 2, mx + 1, i):
                cnt_g[i] -= cnt_g[j]

        # Prefix sum of gcd pair counts
        pref = []
        s = 0
        for i in range(1, mx + 1):
            s += cnt_g[i]
            pref.append(s)

        # Find smallest gcd value whose prefix count > query
        return [bisect_right(pref, q) + 1 for q in queries]