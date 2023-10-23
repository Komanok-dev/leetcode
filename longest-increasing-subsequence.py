class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        result = []
        def insert(target):
            left, right = 0, len(result) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if result[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(result):
                result.append(target)
            else:
                result[left] = target
        for num in nums:
            insert(num)
        return len(result)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        result = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    result[i] = max(result[i], 1 + result[j])
        return max(result)
