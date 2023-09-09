# Time: Complexity O(n*t), t is the value of target.
# Space Complexity: O(t)

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()
        for i in range(1, target+1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
                else:
                    break
        return dp[target]
