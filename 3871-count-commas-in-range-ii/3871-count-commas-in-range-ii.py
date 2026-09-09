class Solution:
    def countCommas(self, n):
        count = 0
        power = 1000

        while power <= n:
            count += n - power + 1
            power *= 1000

        return count
        