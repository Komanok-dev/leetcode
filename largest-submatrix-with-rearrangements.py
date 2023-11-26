class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        result = 0
        for col in range(len(matrix[0])):
            height = 0
            for row in range(len(matrix)):
                height = height + 1 if matrix[row][col] == 1 else 0
                matrix[row][col] = height
        for row in matrix:
            row.sort(reverse=True)
            for col in range(len(row)):
                result = max(result, (col+1) * row[col])
        return result
