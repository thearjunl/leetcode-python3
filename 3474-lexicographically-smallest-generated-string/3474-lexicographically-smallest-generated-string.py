class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        sz = n + m - 1
        
        # Each position in the answer string and whether it is modifiable
        ans = [None] * sz          # None means not yet set
        modifiable = [True] * sz   # True if we can change this char later
        
        # 1. Handle all 'T' positions first
        for i, tf in enumerate(str1):
            if tf == 'T':
                for j, c in enumerate(str2):
                    pos = i + j
                    if ans[pos] is not None and ans[pos] != c:
                        return ""  # conflict
                    ans[pos] = c
                    modifiable[pos] = False
        
        # 2. Fill all remaining positions with 'a'
        for i in range(sz):
            if ans[i] is None:
                ans[i] = 'a'
        
        # 3. Helper: check if substring at index i matches str2
        def _match(i: int) -> bool:
            for j, c in enumerate(str2):
                if ans[i + j] != c:
                    return False
            return True
        
        # 4. Helper: find the last modifiable position in window [i, i + m - 1]
        def _lastModifiablePosition(i: int) -> int:
            res = -1
            for j in range(m):
                pos = i + j
                if modifiable[pos]:
                    res = pos
            return res
        
        # 5. Handle all 'F' positions
        for i in range(n):
            if str1[i] == 'F' and _match(i):
                pos = _lastModifiablePosition(i)
                if pos == -1:
                    return ""   # no free char to break the match
                ans[pos] = 'b'  # make it different from str2[pos - i]
                modifiable[pos] = False
        
        return ''.join(ans)