class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        # Suffix array via prefix doubling
        vals = sorted(set(nums))
        comp = {v: i for i, v in enumerate(vals)}
        rank = [comp[x] for x in nums]
        sa = list(range(n))
        k = 1
        while True:
            keys = [rank[i] * (n + 2) + (rank[i + k] + 1 if i + k < n else 0)
                    for i in range(n)]
            sa.sort(key=keys.__getitem__)
            new_rank = [0] * n
            for j in range(1, n):
                new_rank[sa[j]] = new_rank[sa[j - 1]] + (keys[sa[j]] != keys[sa[j - 1]])
            rank = new_rank
            if rank[sa[-1]] == n - 1:
                break
            k <<= 1

        # LCP array (Kasai)
        lcp = [0] * n
        h = 0
        for i in range(n):
            r = rank[i]
            if r > 0:
                j = sa[r - 1]
                while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                    h += 1
                lcp[r] = h
                if h:
                    h -= 1
            else:
                h = 0

        # Shortest unique prefix over all suffixes
        ans = n
        for r in range(n):
            left = lcp[r] if r > 0 else 0
            right = lcp[r + 1] if r + 1 < n else 0
            need = max(left, right) + 1
            if need <= n - sa[r]:
                ans = min(ans, need)
        return ans