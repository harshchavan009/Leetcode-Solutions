class Solution:
    def findLUSlength(self, strs):
        def isSubsequence(s, t):
            i = 0

            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1

            return i == len(s)

        for i in sorted(range(len(strs)), key=lambda x: len(strs[x]), reverse=True):
            uncommon = True

            for j in range(len(strs)):
                if i != j and isSubsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                return len(strs[i])

        return -1