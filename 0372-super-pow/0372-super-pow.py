class Solution:
    def superPow(self, a, b):
        MOD = 1337
        result = 1

        for digit in b:
            result = pow(result, 10, MOD) * pow(a, digit, MOD) % MOD

        return result