from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        if len(matrix) > len(matrix[0]):
            return self.numSubmatrixSumTarget(list(map(list, zip(*matrix))), target)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                matrix[i][j+1] += matrix[i][j]

        result = 0
        for i in range(len(matrix)):
            prefix_sum = [0] * len(matrix[i])
            for j in range(i, len(matrix)):
                lookup = defaultdict(int)
                lookup[0] = 1
                for k in range(len(matrix[j])):
                    prefix_sum[k] += matrix[j][k]
                    if prefix_sum[k] - target in lookup:
                        result += lookup[prefix_sum[k] - target]
                    lookup[prefix_sum[k]] += 1
        return result
