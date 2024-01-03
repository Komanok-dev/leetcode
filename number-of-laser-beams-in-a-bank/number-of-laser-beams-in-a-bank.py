class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev, res = 0, 0
        for row in bank:
            cnt = row.count('1')
            if not cnt:
                continue
            res += (prev * cnt)
            prev = cnt
        return res
