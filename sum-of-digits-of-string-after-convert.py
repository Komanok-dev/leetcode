class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_int = ''
        for i in s:
            s_int += str(ord(i) - 96)
        s_int = int(s_int)
        while k > 0:
            count = 0
            n = s_int
            while n > 0:
                n, d = n // 10, n % 10
                count += d
            s_int = count
            k -= 1
        return s_int
