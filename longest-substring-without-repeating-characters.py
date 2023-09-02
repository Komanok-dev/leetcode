class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        ans = left = right = 0
        for right in range(0, len(s)):
            if s[right] in hash:
                left = max(hash[s[right]] + 1, left)
            hash[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans
