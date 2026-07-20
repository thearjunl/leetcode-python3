from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Sort the costs to buy cheapest ice creams first (greedy approach)
        costs.sort()
        count = 0
        
        # Buy ice cream bars one by one
        for price in costs:
            if coins >= price:
                coins -= price
                count += 1
            else:
                # Can't afford this one, can't afford any more (since array is sorted)
                break
        
        return count