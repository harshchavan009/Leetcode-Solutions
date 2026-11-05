class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h == 0:
                    continue

                # Top and bottom surfaces
                area += 2

                # Four side surfaces
                area += 4 * h

                # Remove overlapping faces with adjacent towers
                if i > 0:
                    area -= 2 * min(h, grid[i - 1][j])

                if j > 0:
                    area -= 2 * min(h, grid[i][j - 1])

        return area