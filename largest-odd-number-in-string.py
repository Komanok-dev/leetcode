class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 == 1:
            return num
        for i in range(-2, -(len(num) + 1), -1):
            if int(num[i]) % 2 == 1:
                return num[:(i+1)]
        return ''
