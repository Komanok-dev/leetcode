class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result, max_count = 0, 0
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            max_count = max(max_count, count[s[i]])
            if result - max_count >= k:
                count[s[i-result]] -= 1
            else:
                result += 1
        return result
