class Solution:
    def minOperations(self, s: str) -> int:
        count = sum(int(c) == i % 2 for i, c in enumerate(s))
        return min(count, len(s) - count)
