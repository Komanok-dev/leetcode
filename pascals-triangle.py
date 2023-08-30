class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        row = [1]
        result = [row]
        for _ in range(numRows):
            row = [x + y for x, y in zip([0] + row, row + [0])]
            result.append(row)
        return result
    
    # Recursion
    def generate2(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        result = self.generate(numRows - 1)
        previous = result[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        result.append(current)
        return result
