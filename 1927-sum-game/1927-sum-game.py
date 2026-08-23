class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        # Calculate sums and number of '?' in each half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Difference between the known digit sums
        diff = left_sum - right_sum

        # Difference in number of '?' characters
        q_diff = left_q - right_q

        # If the number of '?' is odd, Alice makes the final move
        # and can always make the sums unequal.
        if q_diff % 2 != 0:
            return True

        # When the number of '?' is balanced/even, Bob can force
        # equality only when the initial difference can be exactly
        # compensated by the '?' values.
        if diff == 9 * (-q_diff) // 2:
            return False

        return True