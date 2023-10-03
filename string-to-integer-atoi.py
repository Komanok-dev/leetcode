import re


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0

        if len(s) < 1:
            return result
        
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1
        if i == len(s):
            return result
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            if result > INT_MAX:
                return INT_MAX if sign > 0 else INT_MIN

        return result * sign
