class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            temp_index = nums.index(i) + 1
            temp_nums = nums[temp_index:]
            if target - i in temp_nums:
                return [nums.index(i), temp_index + temp_nums.index(target-i)]
