class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        # dp[j] = minimum health needed to reach the princess
        # from the current cell to the destination.
        dp = [float('inf')] * (n + 1)

        # Sentinel values
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                needed = min(dp[j], dp[j + 1]) - dungeon[i][j]

                # Knight must always have at least 1 health
                dp[j] = max(1, needed)

        return dp[0]