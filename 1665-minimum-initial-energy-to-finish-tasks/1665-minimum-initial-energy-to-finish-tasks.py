from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by ascending (actual - minimum) to maximize leftover energy early
        tasks.sort(key=lambda x: x[0] - x[1])
        
        ans = 0
        energy = 0  # Current remaining energy
        
        for actual, minimum in tasks:
            if energy < minimum:
                # Add just enough initial energy to meet requirement
                ans += minimum - energy
                energy = minimum - actual  # Update remaining after task
            else:
                energy -= actual  # Use existing energy
        
        return ans