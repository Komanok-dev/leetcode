from collections import deque


class Solution(object):
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        dp = [[float("inf")] * len(graph) for _ in range(1 << len(graph))]
        q = deque()
        for i in range(len(graph)):
            dp[1 << i][i] = 0
            q.append((1 << i, i))
        while q:
            state, node = q.popleft()
            steps = dp[state][node]
            for nei in graph[node]:
                new_state = state | (1 << nei)
                if dp[new_state][nei] == float("inf"):
                    dp[new_state][nei] = steps+1
                    q.append((new_state, nei))
        return min(dp[-1])
