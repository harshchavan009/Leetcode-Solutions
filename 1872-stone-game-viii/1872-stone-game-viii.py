class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # prefix[i] = sum of stones[0 ... i]
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If Alice takes the first n-1 stones,
        # the score difference is prefix[n-2] - ...
        # Start from the state where all stones except
        # the last one have been merged.
        dp = prefix[n - 1]

        # Work backwards.
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp