class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count1, count2 = 0, 0
        element1, element2 = 0, 1
        for i in range(len(nums)):
            if nums[i] == element1:
                count1 += 1
            elif nums[i] == element2:
                count2 += 1
            elif count1 == 0:
                element1, count1 = nums[i], 1
            elif count2 == 0:
                    element2, count2 = nums[i], 1
            else:
                count1 -= 1
                count2 -= 1
        return [num for num in (element1, element2) if nums.count(num) > len(nums) // 3]
