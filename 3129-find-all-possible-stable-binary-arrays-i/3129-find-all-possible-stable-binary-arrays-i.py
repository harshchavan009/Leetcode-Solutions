from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(z, o, last):
            if z == 0:
                return 1 if last == 1 and o <= limit else 0
            if o == 0:
                return 1 if last == 0 and z <= limit else 0

            if last == 0:
                ans = 0
                for i in range(1, min(limit, z) + 1):
                    ans += dfs(z - i, o, 1)
                return ans % MOD
            else:
                ans = 0
                for i in range(1, min(limit, o) + 1):
                    ans += dfs(z, o - i, 0)
                return ans % MOD

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD