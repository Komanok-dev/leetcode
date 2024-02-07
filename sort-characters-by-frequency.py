from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        result = list(sorted(Counter(s).items(), key=lambda x: x[1], reverse=True))
        return ''.join(item[0] * item[1] for item in result)
