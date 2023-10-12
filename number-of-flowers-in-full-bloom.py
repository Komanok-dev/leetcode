import bisect


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts, ends = [], []
        for s, e in flowers:
            starts.append(s)
            ends.append(e+1)
        starts.sort()
        ends.sort()
        return [bisect.bisect_right(starts, t)-bisect.bisect_right(ends, t) for t in people]
