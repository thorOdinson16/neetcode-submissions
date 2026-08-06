class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                x = stack.pop()
                y = stack.pop()
                z = int(y) + int(x)
                stack.append(z)
            elif tokens[i] == "-":
                x = stack.pop()
                y = stack.pop()
                z = int(y) - int(x)
                stack.append(z)
            elif tokens[i] == "*":
                x = stack.pop()
                y = stack.pop()
                z = int(y) * int(x)
                stack.append(z)
            elif tokens[i] == "/":
                x = stack.pop()
                y = stack.pop()
                z = int(y) / int(x)
                stack.append(int(z))
            else:
                stack.append(tokens[i])
        return int(stack.pop())
