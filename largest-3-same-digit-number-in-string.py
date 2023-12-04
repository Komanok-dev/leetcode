class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        counter = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                counter += 1
            else:
                counter = 1
            if counter == 3:
                result = max(result, num[i] * 3)
        return result
