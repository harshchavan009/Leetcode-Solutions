class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        n = len(nums)

        mid = (n + 1) // 2
        left = arr[:mid][::-1]
        right = arr[mid:][::-1]

        i = 0
        j = 0

        for k in range(n):
            if k % 2 == 0:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1