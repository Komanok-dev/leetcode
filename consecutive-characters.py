class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count, result = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result
