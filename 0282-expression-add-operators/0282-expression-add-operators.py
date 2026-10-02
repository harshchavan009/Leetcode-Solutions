class Solution:
    def addOperators(self, num, target):
        result = []
        n = len(num)

        def backtrack(index, path, value, prev):
            if index == n:
                if value == target:
                    result.append(path)
                return

            for j in range(index, n):
                # No leading zeros
                if j > index and num[index] == '0':
                    break

                cur_str = num[index:j + 1]
                cur = int(cur_str)

                if index == 0:
                    backtrack(j + 1, cur_str, cur, cur)
                else:
                    # +
                    backtrack(
                        j + 1,
                        path + "+" + cur_str,
                        value + cur,
                        cur
                    )

                    # -
                    backtrack(
                        j + 1,
                        path + "-" + cur_str,
                        value - cur,
                        -cur
                    )

                    # *
                    backtrack(
                        j + 1,
                        path + "*" + cur_str,
                        value - prev + prev * cur,
                        prev * cur
                    )

        backtrack(0, "", 0, 0)

        return result