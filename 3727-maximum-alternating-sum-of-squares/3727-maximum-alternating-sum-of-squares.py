class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted(x * x for x in nums)
        mid = len(nums) // 2

        return sum(squares[mid:]) - sum(squares[:mid])