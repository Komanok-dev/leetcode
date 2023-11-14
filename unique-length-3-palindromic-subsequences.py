from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        left = set()
        right = Counter(s)
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    result.add((s[i], c))
            left.add(s[i])
        return len(result)
