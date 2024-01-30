import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operation = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                a = stack.pop()
                b = stack.pop()
                res = operation[token](b, a)
                if token == '/' and b % a and res < 0:
                    res += 1
                stack.append(res)
        return stack[0]
