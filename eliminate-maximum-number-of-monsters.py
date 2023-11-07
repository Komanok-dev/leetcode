class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        invasion = []
        for x, y in zip(dist, speed):
            invasion.append((x - 1) // y + 1)
        invasion.sort()
        for i, j in enumerate(invasion):
            if i >= j:
                return i
        return len(dist)
