class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        if not nums:
            return result
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            print(start, end)
            if nums[i] - 1 != nums[i-1]:
                result.append(f'{start}->{end}' if start != end else str(end))
                start = nums[i]
            end = nums[i]
        result.append(f'{start}->{end}' if start != end else str(end))
        return result
