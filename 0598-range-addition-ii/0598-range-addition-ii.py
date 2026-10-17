class Solution:
    def maxCount(self, m, n, ops):
        min_rows = m
        min_cols = n

        for a, b in ops:
            min_rows = min(min_rows, a)
            min_cols = min(min_cols, b)

        return min_rows * min_cols