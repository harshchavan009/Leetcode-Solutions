class Solution:
    def climbStairs(self, n, costs):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = costs[i - 1] + dp[i - 1] + 1

            if i >= 2:
                dp[i] = min(dp[i], costs[i - 1] + dp[i - 2] + 4)

            if i >= 3:
                dp[i] = min(dp[i], costs[i - 1] + dp[i - 3] + 9)

        return dp[n]