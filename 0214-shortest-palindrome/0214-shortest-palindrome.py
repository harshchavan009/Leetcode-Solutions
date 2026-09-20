class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return s

        rev = s[::-1]
        temp = s + "#" + rev

        # KMP prefix table
        lps = [0] * len(temp)

        for i in range(1, len(temp)):
            j = lps[i - 1]

            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1

            lps[i] = j

        # Longest palindromic prefix length
        k = lps[-1]

        # Add reverse of the remaining suffix in front
        return rev[:len(s) - k] + s