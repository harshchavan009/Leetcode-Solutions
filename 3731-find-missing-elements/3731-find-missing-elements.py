class Solution:
    def findMissingElements(self, nums):
        num_set = set(nums)
        result = []

        start = min(nums)
        end = max(nums)

        for num in range(start, end + 1):
            if num not in num_set:
                result.append(num)

        return result