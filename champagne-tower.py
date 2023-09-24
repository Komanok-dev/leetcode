class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        result = [poured] + [0] * query_row
        for i in range(1, query_row+1):
            for j in reversed(range(i+1)):
                result[j] = max(result[j]-1, 0) / 2.0 + max(result[j-1]-1, 0) / 2.0
        return min(result[query_glass], 1)
