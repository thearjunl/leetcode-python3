class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s[:len(s) // 2]:
            cnt[ord(ch) - 97] += 1

        left = []
        for i in range(26):
            left.append(chr(97 + i) * cnt[i])

        left = "".join(left)
        mid = s[len(s) // 2] if len(s) % 2 else ""
        return left + mid + left[::-1]