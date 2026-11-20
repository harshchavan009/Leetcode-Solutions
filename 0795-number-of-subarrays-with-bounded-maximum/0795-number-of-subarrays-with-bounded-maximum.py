
class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        def count(bound):
            ans = 0
            curr = 0

            for num in nums:
                if num <= bound:
                    curr += 1
                else:
                    curr = 0

                ans += curr

            return ans

        return count(right) - count(left - 1)
