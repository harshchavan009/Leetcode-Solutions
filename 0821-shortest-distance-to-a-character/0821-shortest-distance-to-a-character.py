class Solution:
    def shortestToChar(self, s, c):
        n = len(s)
        result = [n] * n

        prev = -n

        # Left to right
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev

        prev = 2 * n

        # Right to left
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i

            result[i] = min(result[i], prev - i)

        return result