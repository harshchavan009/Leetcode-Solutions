class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(d - mid, 0) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        operations = sum(max(d - level, 0) for d in diff)
        remaining = k - operations

        result = sum(min(d, level) ** 2 for d in diff)
        result -= remaining * (2 * level - 1)

        return result