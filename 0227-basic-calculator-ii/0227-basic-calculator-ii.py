class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    a = stack.pop()

                    # Truncate division toward zero
                    if a < 0:
                        stack.append(-((-a) // num))
                    else:
                        stack.append(a // num)

                sign = ch
                num = 0

        return sum(stack)