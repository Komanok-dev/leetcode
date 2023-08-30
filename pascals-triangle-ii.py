class Solution:
    def getRow(self, rowIndex: int) -> list[list[int]]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
