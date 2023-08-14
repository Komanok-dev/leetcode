class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        memory = 0
        for i in range(1, max(len(a), len(b))+1):
            a_bit = int(a[-i]) if len(a) - i >= 0 else 0
            b_bit = int(b[-i]) if len(b) - i >= 0 else 0
            memory += a_bit + b_bit
            result = str(memory % 2) + result
            memory //= 2
        if memory > 0:
            result = '1' + result
        return result
