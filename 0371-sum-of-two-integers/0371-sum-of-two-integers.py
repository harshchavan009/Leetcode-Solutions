class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a <= max_int:
            return a

        return ~(a ^ mask)