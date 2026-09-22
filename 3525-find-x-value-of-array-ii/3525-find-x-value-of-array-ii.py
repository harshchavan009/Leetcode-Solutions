class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        size = 1
        while size < n:
            size *= 2

        # prod[i] = product of the whole segment modulo k
        prod = [1 % k] * (2 * size)

        # cnt[i][r] = number of non-empty prefixes
        # of this segment having product % k == r
        cnt = [[0] * k for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            v = nums[i] % k
            p = size + i
            prod[p] = v
            cnt[p][v] = 1

        # Merge two children
        for p in range(size - 1, 0, -1):
            left = p * 2
            right = left + 1

            prod[p] = (prod[left] * prod[right]) % k

            for r in range(k):
                cnt[p][r] = cnt[left][r]

            for r in range(k):
                nr = (prod[left] * r) % k
                cnt[p][nr] += cnt[right][r]

        def update(index, value):
            p = size + index
            v = value % k

            prod[p] = v
            cnt[p] = [0] * k
            cnt[p][v] = 1

            p //= 2

            while p:
                left = p * 2
                right = left + 1

                prod[p] = (prod[left] * prod[right]) % k

                for r in range(k):
                    cnt[p][r] = cnt[left][r]

                for r in range(k):
                    nr = (prod[left] * r) % k
                    cnt[p][nr] += cnt[right][r]

                p //= 2

        def merge(a, b):
            # a and b are (product, counts)
            ap, ac = a
            bp, bc = b

            new_prod = (ap * bp) % k
            new_cnt = ac[:]

            for r in range(k):
                new_cnt[(ap * r) % k] += bc[r]

            return new_prod, new_cnt

        def query(left, right):
            left += size
            right += size

            lres = (1 % k, [0] * k)
            rres = (1 % k, [0] * k)

            while left <= right:
                if left % 2 == 1:
                    lres = merge(lres, (prod[left], cnt[left]))
                    left += 1

                if right % 2 == 0:
                    rres = merge((prod[right], cnt[right]), rres)
                    right -= 1

                left //= 2
                right //= 2

            return merge(lres, rres)

        ans = []

        for index, value, start, x in queries:
            update(index, value)

            _, counts = query(start, n - 1)
            ans.append(counts[x])

        return ans