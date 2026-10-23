class Solution:
    def findShortestSubArray(self, nums):
        freq = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            freq[num] = freq.get(num, 0) + 1
            last[num] = i

        degree = max(freq.values())
        result = len(nums)

        for num in freq:
            if freq[num] == degree:
                result = min(result, last[num] - first[num] + 1)

        return result