class Solution:
    def maxProduct(self, words):
        masks = {}
        
        # Store the maximum length for each unique letter mask
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            
            masks[mask] = max(masks.get(mask, 0), len(word))

        items = list(masks.items())
        ans = 0

        for i in range(len(items)):
            mask1, len1 = items[i]

            for j in range(i + 1, len(items)):
                mask2, len2 = items[j]

                if mask1 & mask2 == 0:
                    ans = max(ans, len1 * len2)

        return ans