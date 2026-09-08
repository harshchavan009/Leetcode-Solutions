class Solution:
    def countCommas(self, n):
        count = 0

        for i in range(1000, n + 1):
            count += (len(str(i)) - 1) // 3

        return count