class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        result = []

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        for num in nums2:
            if count.get(num, 0) > 0:
                result.append(num)
                count[num] -= 1

        return result