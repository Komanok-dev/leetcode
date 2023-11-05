class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        while up <= down:
            mid = (up + down) // 2
            if target > matrix[mid][-1]:
                up = mid + 1
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                break
        if not (up <= down):
            return False
        row = (up + down) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
