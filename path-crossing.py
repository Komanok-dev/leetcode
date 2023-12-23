class Solution:
    def isPathCrossing(self, path: str) -> bool:
        road = {
            'N': [0, 1],
            'S': [0, -1],
            'W': [-1, 0],
            'E': [1, 0],
        }
        visited = {(0, 0): 1}
        curr = (0, 0)
        for side in path:
            curr = (curr[0] + road[side][0], curr[1] + road[side][1])
            if visited.get(curr, 0):
                return True
            visited[curr] = 1
        return False


path = "NES"
path = "NESWW"
a = Solution()
print(a.isPathCrossing(path))
