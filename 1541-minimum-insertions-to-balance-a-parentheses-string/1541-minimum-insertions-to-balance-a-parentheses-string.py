class Solution(object):
    def minInsertions(self, s):
        res = 0      # insertions made
        open_ = 0    # unmatched '('
        i, n = 0, len(s)

        while i < n:
            if s[i] == '(':
                open_ += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2           # found a full "))"
                else:
                    res += 1         # lone ')', insert one more ')'
                    i += 1
                if open_ > 0:
                    open_ -= 1       # match with a pending '('
                else:
                    res += 1         # no '(' available, insert one

        return res + 2 * open_