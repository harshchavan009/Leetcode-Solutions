class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        answer = len(nums) + 1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                answer = min(answer, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if answer == len(nums) + 1:
            return 0

        return answer