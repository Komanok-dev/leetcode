class Solution:
    def isValid(self, s: str) -> bool:
        opening = '({['
        closing = ')}]'
        parenteses = {')': '(', '}': '{', ']': '['}
        if s[0] in closing or s[-1] in opening:
            return False
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif len(stack) < 1 or stack.pop() != parenteses[i]:
                return False
        return True if len(stack) == 0 else False
    