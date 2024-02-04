from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, remain = Counter(t), len(t)
        i, left, right = 0, -1, -1
        for j, c in enumerate(s):
            remain -= count[c] > 0
            count[c] -= 1
            if remain:
                continue
            while count[s[i]] < 0:
                count[s[i]] += 1
                i += 1
            if right == -1 or j-i+1 < right - left + 1:
                left, right = i, j
        return s[left:right+1]
