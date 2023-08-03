class Solution:
    # most efficient

    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False


    # without converting to string

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return x == reversed_num or x == reversed_num // 10
