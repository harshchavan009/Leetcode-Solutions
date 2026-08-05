class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if current number is too large
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                # Move to the next index (each number can be used only once)
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result