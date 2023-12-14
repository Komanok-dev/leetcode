class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        row = [0] * len(grid)
        col = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(diff)):
            for j in range(len(diff[0])):
                diff[i][j] = 2 * (row[i] + col[j]) - len(diff) - len(diff[0])
        return diff
