class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # buckets[i] = numbers appearing i times
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result