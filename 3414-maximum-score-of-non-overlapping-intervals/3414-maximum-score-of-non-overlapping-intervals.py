from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval whose left endpoint is > arr[i].right
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_left(starts, arr[i][1] + 1)

        # dp[i][k] = best result using intervals from i onward,
        # choosing at most k intervals.
        #
        # Store (score, tuple of indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            # Higher score is better.
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # For equal score, lexicographically smaller indices.
            if a[1] < b[1]:
                return a
            return b

        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]

            for k in range(1, 5):
                # Option 1: skip this interval
                best = dp[i + 1][k]

                # Option 2: take this interval
                next_score, next_indices = dp[nxt[i]][k - 1]

                candidate = (
                    w + next_score,
                    tuple(sorted((idx,) + next_indices))
                )

                best = better(best, candidate)
                dp[i][k] = best

            # k = 0 means we cannot take anything
            dp[i][0] = (0, ())

        return list(dp[0][4][1])