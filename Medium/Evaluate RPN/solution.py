'''
Time complexity O(n)
Space complexity O(n)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '/':
                    stack.append(int(a/b))

        return stack[0]