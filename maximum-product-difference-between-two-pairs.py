class Solution:
    # Time O(n)
    # Space O(1)
    def maxProductDifference(self, nums: list[int]) -> int:
        min1, min2 = float('inf'), float('inf')
        max1, max2 = 0, 0
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return max1 * max2 - min1 * min2 


    # Time O(nlogn)
    # Space O(1)
    def maxProductDifference2(self, nums: list[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
