class Solution:
    def uniformArray(self, nums1):
        minimum = min(nums1)

        # If all numbers already have the same parity
        all_even = True
        all_odd = True

        for x in nums1:
            if x % 2 == 0:
                all_odd = False
            else:
                all_even = False

        if all_even or all_odd:
            return True

        # Mixed parity is possible only when the smallest
        # number is odd. Then every even number can subtract
        # this smaller odd number to become odd.
        return minimum % 2 == 1