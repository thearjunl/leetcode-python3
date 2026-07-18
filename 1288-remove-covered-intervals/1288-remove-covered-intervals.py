from typing import List
from math import inf

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start asc, and for equal start by end desc
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        ans = 0
        prev_end = -inf  # farthest right endpoint seen so far
        
        for _, end in intervals:
            # If current end is greater than all previous ends,
            # it is not covered by any previous interval.
            if end > prev_end:
                ans += 1
                prev_end = end
        
        return ans