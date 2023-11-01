class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def print_board():
            for i in range(len(board)):
                if i % 3 == 0:
                    print('-------------------------')
                for j in range(len(board[0])):
                    if j % 3 == 0:
                        print('| ', end='')
                    print(board[i][j], end=' ')
                print('|', end='')
                print()
            print('-------------------------')
        
        def is_valid(row, col, num):
            num = str(num)
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

        def solver():
            find = find_empty()
            if not find:
                return True
            row, col = find
            for num in range(1, 10):
                if is_valid(row, col, num):
                    board[row][col] = str(num)
                    if solver():
                        return True
                    board[row][col] = '.'

        def find_empty():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        return i, j
        print_board()
        solver()



        # check code
        print_board()
        return board


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
a = Solution()
result = a.solveSudoku(board)

assert output == result
