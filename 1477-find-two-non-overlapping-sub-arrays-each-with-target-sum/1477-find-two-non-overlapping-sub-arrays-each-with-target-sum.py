class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # that ends at or before index i
        best = [float('inf')] * n

        left = 0
        current_sum = 0
        answer = float('inf')

        for right in range(n):
            current_sum += arr[right]

            # Since all arr[i] are positive, use sliding window
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                # Need a previous non-overlapping subarray.
                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])

            # Carry forward the best subarray seen so far
            if right == 0:
                best[right] = (
                    right - left + 1 if current_sum == target
                    else float('inf')
                )
            else:
                best[right] = best[right - 1]

                if current_sum == target:
                    best[right] = min(
                        best[right],
                        right - left + 1
                    )

        return -1 if answer == float('inf') else answer