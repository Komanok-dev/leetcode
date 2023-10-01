class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
                if absent == 2:
                    return False
            if i < len(s) - 2 and s[i] == s[i+1] == s[i+2] == 'L':
                return False
        return True

    def checkRecord2(self, s: str) -> bool:
        absent, late = 0, 0
        for c in s:
            if c == 'A':
                absent += 1
                late = 0
            elif c == 'L':
                late += 1
            else:
                late = 0
            if late >= 3 or absent >= 2:
                return False
        return True

    def checkRecord3(self, s: str) -> bool:
        return False if 'LLL' in s or s.count('A') >= 2 else True
