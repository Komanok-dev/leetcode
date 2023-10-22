class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        l = r = k
        result = nums[k]
        cursor = nums[k]
        while l > 0 or r < len(nums) - 1:
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < len(nums) - 1 else 0
            if left > right:
                l -= 1
                cursor = min(cursor, left)
            else:
                r += 1
                cursor = min(cursor, right)
            result = max(result, cursor * (r -l + 1))
        return result
    