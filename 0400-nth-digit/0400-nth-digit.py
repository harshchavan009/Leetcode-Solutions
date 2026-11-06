class Solution:
    def findNthDigit(self, n):
        digits = 1
        start = 1
        count = 9

        # Find the group containing the nth digit
        while n > digits * count:
            n -= digits * count
            digits += 1
            start *= 10
            count *= 10

        # Find the actual number
        num = start + (n - 1) // digits

        # Find the digit's position
        index = (n - 1) % digits

        return int(str(num)[index])