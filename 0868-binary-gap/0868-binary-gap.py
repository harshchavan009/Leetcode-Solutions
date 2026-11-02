class Solution:
    def binaryGap(self, n):
        last = -1
        max_distance = 0
        position = 0

        while n > 0:
            if n & 1:
                if last != -1:
                    max_distance = max(max_distance, position - last)

                last = position

            n >>= 1
            position += 1

        return max_distance