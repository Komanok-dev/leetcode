from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = Counter(s)
        result = []
        stack = set()
        for letter in s:
            if letter not in stack:
                while result and result[-1] > letter and letters[result[-1]]:
                    stack.remove(result.pop())
                result += letter
                stack.add(letter)
            letters[letter] -= 1
        return ''.join(result)
