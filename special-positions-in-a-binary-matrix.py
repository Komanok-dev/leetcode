class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        count = 0
        rows, cols = [0] * len(mat), [0] * len(mat[0])
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j] == rows[i] == cols[j] == 1:
                    count += 1
        return count
