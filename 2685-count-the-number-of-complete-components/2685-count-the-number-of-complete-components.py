from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n

        def dfs(node: int, counts: List[int]) -> None:
            # counts[0] = number of vertices v
            # counts[1] = sum of degrees e (each incident edge counted once per endpoint)
            visited[node] = True
            counts[0] += 1
            counts[1] += len(graph[node])
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, counts)

        complete_components = 0

        # Explore each component
        for i in range(n):
            if not visited[i]:
                v_e = [0, 0]  # [v, e]
                dfs(i, v_e)
                v, e = v_e
                # For a complete component: sum of degrees e == v * (v - 1)
                if e == v * (v - 1):
                    complete_components += 1

        return complete_components