class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                result[i][j] = matrix[j][i]
        return result
