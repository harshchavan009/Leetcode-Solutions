class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0

        # Position of the most recent '*'
        star = -1

        # Position in s that the '*' is currently matching up to
        match = 0

        while i < len(s):
            # Case 1: Current characters match
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1

            # Case 2: Current pattern character is '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: Mismatch, but there was a previous '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: No possible match
            else:
                return False

        # Remaining pattern characters must all be '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)