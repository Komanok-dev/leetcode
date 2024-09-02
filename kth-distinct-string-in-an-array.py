from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        cnt = Counter(arr)
        for c in arr:
            if cnt[c] == 1:
                k -= 1
            if k == 0:
                return c
        return ''
