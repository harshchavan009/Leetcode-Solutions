class Solution:
    def largeGroupPositions(self, s):
        result = []
        n = len(s)
        i = 0

        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1

            if i - start >= 3:
                result.append([start, i - 1])

        return result