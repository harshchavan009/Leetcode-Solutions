class Solution:
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1

        papers = 0

        for h in range(n, -1, -1):
            papers += count[h]

            if papers >= h:
                return h

        return 0