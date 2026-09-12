class Solution:
    def totalNQueens(self, n):
        cols = set()
        diag1 = set()
        diag2 = set()

        result = [0]

        def backtrack(row):
            if row == n:
                result[0] += 1
                return

            for col in range(n):
                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return result[0]