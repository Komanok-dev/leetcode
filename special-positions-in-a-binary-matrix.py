class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows, cols = [0]*len(mat), [0]*len(mat[0])
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        print(rows)
        print(cols)
        
        result = 0
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j] == rows[i] == cols[j] == 1:
                    result += 1
        return result


a = Solution()
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(a.numSpecial(mat))