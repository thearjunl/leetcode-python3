from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        suspicious = set([k])
        q = deque([k])

        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in suspicious:
                    suspicious.add(v)
                    q.append(v)

        for u in range(n):
            if u in suspicious:
                continue
            for v in graph[u]:
                if v in suspicious:
                    return list(range(n))

        return [i for i in range(n) if i not in suspicious]