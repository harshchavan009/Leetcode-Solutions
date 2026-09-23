class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        n = len(nums)

        if target < 0:
            return -1

        # Find the longest subarray with sum = target
        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return n - max_len