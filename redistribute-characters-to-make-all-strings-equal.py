from collections import defaultdict


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        cnt = defaultdict(int)
        for word in words:
            for c in word:
                cnt[c] += 1
        return all(l % len(words) == 0 for l in cnt.values())
