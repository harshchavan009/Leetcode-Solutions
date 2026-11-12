class Solution:
    def longestMonotonicSubarray(self, nums):
        increasing = 1
        decreasing = 1
        result = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1

            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1

            else:
                increasing = 1
                decreasing = 1

            result = max(result, increasing, decreasing)

        return result
        