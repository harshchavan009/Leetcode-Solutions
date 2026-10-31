class Solution:
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            skip_s = 0
            skip_t = 0

            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            char_s = s[i] if i >= 0 else ''
            char_t = t[j] if j >= 0 else ''

            if char_s != char_t:
                return False

            i -= 1
            j -= 1

        return True