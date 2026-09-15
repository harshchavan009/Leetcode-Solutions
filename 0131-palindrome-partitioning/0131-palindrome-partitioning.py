class Solution:
    def partition(self, s):
        result = []
        path = []

        def backtrack(start):
            # Reached the end of the string
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                # Check if the substring is a palindrome
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)

        return result