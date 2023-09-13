from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        result = 0
        lookup = set()
        for k,v in count.items():
            while v > 0 and v in lookup:
                v -= 1
                result += 1
            lookup.add(v)
        return result
