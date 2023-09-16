class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result, u = 0, 0
        dist = [float("inf")] * len(points)
        lookup = set()
        for _ in range(len(points)-1):
            x0, y0 = points[u]
            lookup.add(u)
            for v, (x, y) in enumerate(points):
                if v in lookup:
                    continue
                dist[v] = min(dist[v], abs(x-x0) + abs(y-y0))
            val, u = min((val, v) for v, val in enumerate(dist)) 
            dist[u] = float("inf")
            result += val
        return result
