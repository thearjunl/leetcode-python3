from typing import List
from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        used = set()

        for i, ch in enumerate(s):
            if ch in used:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                used.remove(stack.pop())

            stack.append(ch)
            used.add(ch)

        return "".join(stack)