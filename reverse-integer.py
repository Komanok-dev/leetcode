class Solution:
    def reverse(self, x: int) -> int:
        rev_int = 0
        if x < 0:
            x = x * -1
            multiplier = -1
        else:
            multiplier = 1
        while x:
            rev_int = rev_int * 10 + x % 10
            x //= 10
        rev_int = rev_int * multiplier
        return 0 if (rev_int > 2**31 -1 or rev_int < -2**31) else rev_int

    def reverse2(self, x: int) -> int:
        if x < 0:
            x = -int(str(x).replace('-', '')[::-1])
        else:
            x = int(str(x)[::-1])
        return 0 if (x > 2**31 -1 or x < -2**31) else x
