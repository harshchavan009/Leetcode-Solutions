class Solution:
    def braceExpansionII(self, expression):
        i = [0]

        def parse():
            # Parse a concatenation of expressions
            res = {""}

            while i[0] < len(expression) and expression[i[0]] not in "},":
                if expression[i[0]] == "{":
                    i[0] += 1

                    # Parse union inside braces
                    cur = parse()
                    union = set(cur)

                    while i[0] < len(expression) and expression[i[0]] == ",":
                        i[0] += 1
                        part = parse()
                        union |= part

                    i[0] += 1  # skip '}'
                    part = union

                else:
                    part = {expression[i[0]]}
                    i[0] += 1

                # Cartesian product for concatenation
                res = {a + b for a in res for b in part}

            return res

        return sorted(parse())