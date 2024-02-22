from collections import Counter


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        table = dict([(i, 0) for i in range(1, n + 1)])
        count = Counter([i[1] for i in trust])
        for check in trust:
            table[check[0]] += 1
        table = sorted(table.items(), key=lambda x: x[1])
        return table[0][0] if table[0][1] == 0 and count[table[0][0]] == n - 1 else -1
