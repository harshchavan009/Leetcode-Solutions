class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        dp = [1] + [0] * (n - 1)

        for i in range(m):
            left = 0

            for j in range(n):
                if grid[i][j] == 1:
                    # Mirror: swap incoming path directions
                    left, dp[j] = dp[j], left
                else:
                    # Empty cell: combine paths from left and above
                    left = (left + dp[j]) % MOD
                    dp[j] = left

        return left