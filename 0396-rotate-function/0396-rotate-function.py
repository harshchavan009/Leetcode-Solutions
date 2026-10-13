class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)

        current = sum(i * nums[i] for i in range(n))
        maximum = current

        for i in range(n - 1, 0, -1):
            current = current + total - n * nums[i]
            maximum = max(maximum, current)

        return maximum