class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Product of all elements to the left
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Product of all elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer