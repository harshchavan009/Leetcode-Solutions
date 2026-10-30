import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'[a-z]+', paragraph.lower())
        banned_set = set(banned)

        count = Counter(words)

        for word, freq in count.most_common():
            if word not in banned_set:
                return word