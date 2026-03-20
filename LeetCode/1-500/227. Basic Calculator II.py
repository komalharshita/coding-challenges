class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == '+':
                stack.append(v)
            elif op == '-':
                stack.append(-v)
            elif op == '*':
                stack.append(stack.pop() * v)
            elif op == '/':
                last = stack.pop()
                if last // v < 0 and last % v != 0:
                    stack.append(last // v + 1) 
                else:
                    stack.append(last // v)

        i, num, stack, sign = 0, 0, [], "+"

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+-*/":
                update(sign, num)
                num, sign = 0, s[i]
            elif s[i] == "(":
                num, j = self.calculate(s[i + 1:])
                i = i + j
            elif s[i] == ")":
                update(sign, num)
                return sum(stack), i + 1
            i += 1
        update(sign, num)
        return sum(stack)