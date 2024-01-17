from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = Counter(arr).values()
        return len(count) == len(set(count))
