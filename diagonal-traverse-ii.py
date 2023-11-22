class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if len(result) > i+j:
                    result[i+j].append(nums[i][j])
                else:
                    result.append([nums[i][j]])
        return [num for row in result for num in reversed(row)]
