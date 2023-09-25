class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                return t[i]
            i += 1
        return t[len(s)]
