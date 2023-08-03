class Solution:
    ROMANS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        int_s = list(map(lambda x: self.ROMANS[x], s))
        for i in range(len(int_s)-1):
            if int_s[i] < int_s[i+1]:
                int_s[i] = int_s[i] * -1
        return sum(int_s)

    def romanToInt2(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1):
            if self.ROMANS[s[i]] < self.ROMANS[s[i+1]]:
                result -= self.ROMANS[s[i]]
            else:
                result += self.ROMANS[s[i]]
        result += self.ROMANS[s[i+1]]
        return result
