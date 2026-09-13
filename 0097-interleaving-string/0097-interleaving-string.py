class Solution:
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)

        # Total length must match
        if m + n != len(s3):
            return False

        # dp[j] = whether s3[:i+j] can be formed
        # using s1[:i] and s2[:j]
        dp = [False] * (n + 1)
        dp[0] = True

        # First row
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # First column
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                index = i + j - 1

                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[index]) or
                    (dp[j - 1] and s2[j - 1] == s3[index])
                )

        return dp[n]