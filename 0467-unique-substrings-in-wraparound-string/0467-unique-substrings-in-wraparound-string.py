class Solution:
    def findSubstringInWraproundString(self, s):
        dp = [0] * 26
        current = 0

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                current += 1
            else:
                current = 1

            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], current)

        return sum(dp)