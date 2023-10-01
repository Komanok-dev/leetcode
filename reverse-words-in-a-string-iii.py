class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s[::-1].split()))


s = "Let's take LeetCode contest"
# "s'teL ekat edoCteeL tsetnoc
A = Solution()
print(A.reverseWords(s))