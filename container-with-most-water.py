class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        volume = []
        while left < right:
            if height[left] <= height[right]:
                volume.append(height[left] * (right-left))
                left += 1
            else:
                volume.append(height[right] * (right-left))
                right -= 1
        return max(volume)
