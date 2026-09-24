class Solution:
    def lengthOfLIS(self, nums):
        subsequence = []

        for num in nums:
            left = 0
            right = len(subsequence)

            # Binary search for first element >= num
            while left < right:
                mid = (left + right) // 2

                if subsequence[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[left] = num

        return len(subsequence)