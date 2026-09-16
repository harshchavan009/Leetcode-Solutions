class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()

                # Division must truncate toward zero
                if a * b < 0:
                    stack.append(-(abs(a) // abs(b)))
                else:
                    stack.append(abs(a) // abs(b))

            else:
                stack.append(int(token))

        return stack[0]