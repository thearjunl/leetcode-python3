from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        stack = []
        
        # Sort indices by positions (left to right)
        indices.sort(key=lambda i: positions[i])
        
        for curr in indices:
            if directions[curr] == 'R':
                stack.append(curr)
            else:
                # Collide with right-moving robots
                while stack and healths[curr] > 0:
                    top = stack.pop()
                    
                    if healths[top] > healths[curr]:
                        # Right robot survives
                        healths[top] -= 1
                        healths[curr] = 0
                        stack.append(top)
                        break
                    elif healths[top] < healths[curr]:
                        # Left robot survives
                        healths[curr] -= 1
                        healths[top] = 0
                    else:
                        # Both destroyed
                        healths[curr] = 0
                        healths[top] = 0
        
        # Collect surviving healths in original order
        result = [h for h in healths if h > 0]
        return result