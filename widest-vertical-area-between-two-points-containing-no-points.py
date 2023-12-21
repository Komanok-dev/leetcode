class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points = sorted(x for x, y in points)
        return max([points[i] - points[i-1] for i in range(1, len(points))])
