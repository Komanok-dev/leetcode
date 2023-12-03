class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        result = 0
        for point in range(1, len(points)):
            result += max(
                abs(points[point][0] - points[point-1][0]),
                abs(points[point][1] - points[point-1][1]),
            )
        return result
