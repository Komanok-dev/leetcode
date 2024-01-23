from collections import Counter


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        chars = set()

        def count(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(chars)
            result = 0
            if not count(chars, arr[i]):
                for c in arr[i]:
                    chars.add(c)
                result = backtrack(i + 1)
                for c in arr[i]:
                    chars.remove(c)
            return max(result, backtrack(i + 1))

        return backtrack(0)
