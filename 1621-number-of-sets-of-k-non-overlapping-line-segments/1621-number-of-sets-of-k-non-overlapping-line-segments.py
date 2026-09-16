class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        # Answer = C(n + k - 1, 2 * k)
        r = 2 * k
        N = n + k - 1

        numerator = 1
        denominator = 1

        for i in range(1, r + 1):
            numerator = numerator * (N - r + i) % MOD
            denominator = denominator * i % MOD

        return numerator * pow(denominator, MOD - 2, MOD) % MOD