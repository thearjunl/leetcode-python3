from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # Initial health after stepping on (0,0)
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False

        # Directions: up, down, left, right
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        # BFS queue: (row, col, remaining_health)
        q = deque([(0, 0, start_health)])
        # We must track health as part of state; visiting same cell with higher health matters
        seen = {(0, 0, start_health)}

        while q:
            i, j, h = q.popleft()

            # If we reach bottom-right with positive health, it's safe
            if i == m - 1 and j == n - 1 and h > 0:
                return True

            for dx, dy in DIRS:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                next_health = h - grid[x][y]
                if next_health <= 0:
                    continue

                state = (x, y, next_health)
                if state in seen:
                    continue

                seen.add(state)
                q.append((x, y, next_health))

        return False