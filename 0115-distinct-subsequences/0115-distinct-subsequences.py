class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[j] = number of ways to form t[:j] using a prefix of s.
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t can always be formed

        for i in range(1, m + 1):
            prev = dp[:]  # copy of previous row (dp[i-1][*])
            for j in range(1, n + 1):
                dp[j] = prev[j]  # skip s[i-1]
                if s[i - 1] == t[j - 1]:
                    dp[j] += prev[j - 1]  # use s[i-1] to match t[j-1]

        return dp[n]