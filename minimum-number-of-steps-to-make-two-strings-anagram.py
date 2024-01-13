from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        difference = Counter(s) - Counter(t)
        return sum(difference.values())
