from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        res = defaultdict(int)
        for match in matches:
            res[match[0]] += 0
            res[match[1]] += 1
        return sorted([k for k,v in res.items() if v == 0]), sorted([k for k,v in res.items() if v == 1])
