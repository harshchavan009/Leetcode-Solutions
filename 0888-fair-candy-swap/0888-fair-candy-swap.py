class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)

        diff = (sum_b - sum_a) // 2
        bob_set = set(bobSizes)

        for a in aliceSizes:
            b = a + diff

            if b in bob_set:
                return [a, b]

        return []