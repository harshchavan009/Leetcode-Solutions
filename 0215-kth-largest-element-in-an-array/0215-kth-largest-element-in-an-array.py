import random

class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            low = left
            i = left
            high = right

            # 3-way partition
            while i <= high:
                if nums[i] < pivot:
                    nums[low], nums[i] = nums[i], nums[low]
                    low += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[high] = nums[high], nums[i]
                    high -= 1
                else:
                    i += 1

            if target < low:
                right = low - 1
            elif target > high:
                left = high + 1
            else:
                return pivot