class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first, second = 0, 0
        for i in range(2, len(cost)+1):
            temp = first
            first = min(first + cost[i-1], second + cost[i-2])
            second = temp
        return first
