class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            if freq[ch] < k:
                parts = s.split(ch)
                best = 0

                for part in parts:
                    length = self.longestSubstring(part, k)
                    best = max(best, length)

                return best

        return len(s)