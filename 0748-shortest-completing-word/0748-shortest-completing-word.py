from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        result = None

        for word in words:
            counts = Counter(word)

            if all(counts[c] >= required[c] for c in required):
                if result is None or len(word) < len(result):
                    result = word

        return result