class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = None

            for start in range(0, n, k):
                block = nums[start:start + k]

                descents = 0
                for i in range(k):
                    if block[i] > block[(i + 1) % k]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

                block_min = min(block)
                block_max = max(block)

                if prev_max is not None and prev_max > block_min:
                    valid = False
                    break

                prev_max = block_max

            if valid:
                answer += k

        return answer