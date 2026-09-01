from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n = len(classroom)
        m = len(classroom[0])

        # Map each litter 'L' to a bit index.
        litter_id = {}
        k = 0
        start = None

        for i in range(n):
            for j in range(m):
                cell = classroom[i][j]
                if cell == "L":
                    litter_id[(i, j)] = k
                    k += 1
                elif cell == "S":
                    start = (i, j)

        full_mask = (1 << k) - 1

        # State: (row, col, mask, energy)
        # We want minimum steps to reach mask == full_mask.
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))  # row, col, mask, energy, steps

        # visited[(row, col, mask)] = max_energy seen at this state
        visited = {}

        while q:
            r, c, mask, e, steps = q.popleft()

            if mask == full_mask:
                return steps

            if e <= 0:
                continue

            # Prune if we've seen this (r,c,mask) with >= energy before.
            key = (r, c, mask)
            if visited.get(key, -1) >= e:
                continue
            visited[key] = e

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                cell = classroom[nr][nc]

                if cell == "X":
                    continue

                new_mask = mask
                if cell == "L":
                    new_mask = mask | (1 << litter_id[(nr, nc)])

                new_energy = e - 1
                if cell == "R":
                    new_energy = energy

                q.append((nr, nc, new_mask, new_energy, steps + 1))

        return -1