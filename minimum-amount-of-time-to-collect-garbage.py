class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        result = 0
        for c in 'MPG':
            curr = 0
            for i in range(len(garbage)):
                cnt = garbage[i].count(c)
                print(cnt)
                if cnt:
                    result += curr + cnt
                    curr = 0
                if i < len(travel):
                    curr += travel[i]
        return result
