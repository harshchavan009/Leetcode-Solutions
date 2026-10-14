class Solution:
    def maxSumOfSquares(self, num, sum):
        if num * 9 < sum:
            return ""

        nines, remainder = divmod(sum, 9)

        result = "9" * nines

        if remainder > 0:
            result += str(remainder)

        result += "0" * (num - len(result))

        return result