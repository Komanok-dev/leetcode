class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            return self.maxDotProduct(nums2, nums1)
        dp = [[0]*len(nums2) for _ in range(2)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i%2][j] = nums1[i] * nums2[j]
                if i and j:
                    dp[i%2][j] += max(dp[(i-1)%2][j-1], 0)
                if i:
                    dp[i%2][j] = max(dp[i%2][j], dp[(i-1)%2][j])
                if j:
                    dp[i%2][j] = max(dp[i%2][j], dp[i%2][j-1])
        return dp[(len(nums1)-1)%2][-1]
