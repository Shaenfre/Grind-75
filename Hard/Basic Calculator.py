'''
Time complexity O(n)
Space complexity O(n)
TODO: Basic Calculator 2 and 3
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        current = 0
        s = "(" + s + ")"

        for c in s:
            if c == " ":
                continue
            elif c == "+":
                res += sign * current
                current = 0
                sign = 1
            elif c == "-":
                res += sign * current
                current = 0
                sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * current
                sign = stack.pop()
                res *= sign
                current = stack.pop()
                res += current 
                current = 0
                sign = 1
            else:
                current = current * 10 + int(c)
            # print(stack)

        return res