
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxLength(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                product *= x
                g = self.gcd(g, x)
                l = (l // self.gcd(l, x)) * x

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans
