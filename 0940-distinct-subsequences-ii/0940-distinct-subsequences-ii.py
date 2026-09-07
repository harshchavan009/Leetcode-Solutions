class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007
        end = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')
            end[i] = (1 + sum(end)) % MOD

        return sum(end) % MOD