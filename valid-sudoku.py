class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def is_valid(row, col, num):
            board[row][col] = '.'
            if num in board[row]:
                return False
            for i in range(len(board)):
                if board[i][col] == num:
                    return False
            for i in range(row // 3 * 3, row // 3 * 3 + 3):
                for j in range(col // 3 * 3, col // 3 * 3 + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if not is_valid(i, j, board[i][j]):
                    return False
        return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a = Solution()
print(a.isValidSudoku(board))