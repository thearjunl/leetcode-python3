class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Combinatorial formula: C(n + k - 1, 2k)
        N = n + k - 1
        R = 2 * k

        if R > N:
            return 0

        # Compute C(N, R) modulo MOD
        ans = 1
        for i in range(1, R + 1):
            ans = ans * (N - i + 1) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans
        