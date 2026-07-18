from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        def dfs(r: int, c: int, parent_r: int, parent_c: int) -> bool:
            visited[r][c] = True
            val = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Out of bounds or different char or parent cell
                if (nr < 0 or nr >= m or nc < 0 or nc >= n or
                    grid[nr][nc] != val or
                    (nr == parent_r and nc == parent_c)):
                    continue
                if visited[nr][nc]:
                    return True  # cycle found
                if dfs(nr, nc, r, c):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):  # no parent initially
                        return True
        return False