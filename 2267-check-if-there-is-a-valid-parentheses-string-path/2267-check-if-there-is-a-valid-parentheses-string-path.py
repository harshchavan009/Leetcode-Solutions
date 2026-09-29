class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # A valid parenthesis string must start with '('
        # and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        memo = {}

        def dfs(r, c, balance):
            key = (r, c, balance)

            if key in memo:
                return memo[key]

            # Use current cell
            if grid[r][c] == '(':
                new_balance = balance + 1
            else:
                new_balance = balance - 1

            # Balance can never become negative
            if new_balance < 0:
                memo[key] = False
                return False

            # Number of cells remaining after current cell
            remaining = (m - 1 - r) + (n - 1 - c)

            # Not enough cells left to close all '('
            if new_balance > remaining:
                memo[key] = False
                return False

            # Reached bottom-right
            if r == m - 1 and c == n - 1:
                memo[key] = (new_balance == 0)
                return memo[key]

            # Move down
            if r + 1 < m and dfs(r + 1, c, new_balance):
                memo[key] = True
                return True

            # Move right
            if c + 1 < n and dfs(r, c + 1, new_balance):
                memo[key] = True
                return True

            memo[key] = False
            return False

        return dfs(0, 0, 0)