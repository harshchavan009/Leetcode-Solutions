class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            a = num % k
            ndp = [0] * k

            # Start a new subarray
            ndp[a] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    ndp[(r * a) % k] += dp[r]

            dp = ndp

            # Count all subarrays ending at this index
            for r in range(k):
                result[r] += dp[r]

        return result