from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequency of each character in text
        cnt = Counter(text)
        
        # Each balloon needs 2 'l's and 2 'o's, so divide their counts by 2
        cnt['l'] >>= 1  # Same as cnt['l'] //= 2
        cnt['o'] >>= 1  # Same as cnt['o'] //= 2
        
        # Return minimum count of required characters: 'b', 'a', 'l', 'o', 'n'
        return min(cnt[c] for c in 'balon')