class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # Precompute all proper divisors for each length
        divisors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for length in range(2, n - i + 1):
                best = INF

                for d in divisors[length]:
                    changes = 0

                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                    if best == 0:
                        break

                cost[i][i + length - 1] = best

        # DP: minimum changes to partition first i characters
        # into exactly j semi-palindromes
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    if dp[parts - 1][start] == INF:
                        continue

                    candidate = (
                        dp[parts - 1][start]
                        + cost[start][end - 1]
                    )

                    dp[parts][end] = min(
                        dp[parts][end],
                        candidate
                    )

        return dp[k][n]