class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]

        if original == color:
            return image

        stack = [(sr, sc)]
        image[sr][sc] = color

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            r, c = stack.pop()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                        and image[nr][nc] == original):
                    image[nr][nc] = color
                    stack.append((nr, nc))

        return image