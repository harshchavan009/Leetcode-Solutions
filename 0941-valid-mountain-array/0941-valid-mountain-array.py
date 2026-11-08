class Solution:
    def validMountainArray(self, arr):
        n = len(arr)

        if n < 3:
            return False

        i = 0

        # Climb up
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be first or last
        if i == 0 or i == n - 1:
            return False

        # Climb down
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1