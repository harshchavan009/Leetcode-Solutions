class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Bucket size
        bucket_size = max(1, (max_val - min_val) // (n - 1))

        # Number of buckets
        bucket_count = (max_val - min_val) // bucket_size + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        used = [False] * bucket_count

        # Put numbers into buckets
        for num in nums:
            index = (num - min_val) // bucket_size

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
            used[index] = True

        # Find maximum gap between non-empty buckets
        max_gap = 0
        previous_max = min_val

        for i in range(bucket_count):
            if not used[i]:
                continue

            max_gap = max(max_gap, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]

        return max_gap