class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        size = len(values)
        rank = {v: i + 1 for i, v in enumerate(values)}

        count_bit = [0] * (size + 1)
        sum_bit = [0] * (size + 1)

        def update(bit, i, delta):
            while i <= size:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        # Find the kth smallest element
        def find_kth(kth):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= size and count_bit[nxt] < kth:
                    idx = nxt
                    kth -= count_bit[nxt]

                step >>= 1

            return idx + 1

        def add_number(num, delta):
            idx = rank[num]
            update(count_bit, idx, delta)
            update(sum_bit, idx, num * delta)

        # Initialize the first window
        window_sum = sum(nums[:x])

        for num in nums[:x]:
            add_number(num, 1)

        # Calculate the minimum cost for every window
        costs = []

        for start in range(n - x + 1):
            median_idx = find_kth((x + 1) // 2)
            median = values[median_idx - 1]

            left_count = query(count_bit, median_idx)
            left_sum = query(sum_bit, median_idx)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide the window
            if start < n - x:
                add_number(nums[start], -1)
                add_number(nums[start + x], 1)

                window_sum += nums[start + x] - nums[start]

        # Dynamic Programming
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip the current position
                curr[i] = curr[i - 1]

                # Select a window of size x
                if i >= x:
                    candidate = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]