class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))

                if img2[i][j] == 1:
                    ones2.append((i, j))

        shifts = {}

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r2 - r1
                dc = c2 - c1

                key = (dr, dc)
                shifts[key] = shifts.get(key, 0) + 1

        if not shifts:
            return 0

        return max(shifts.values())