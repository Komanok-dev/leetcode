class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        double_s = (s + s)[1:-1]
        return double_s.find(s) != -1
    

    def repeatedSubstringPattern2(self, s: str) -> bool:
        sub_s = ''
        for i in s:
            if i in sub_s:
                if (
                    len(s) % len(sub_s) == 0
                    and s.count(sub_s) == len(s) // len(sub_s)
                ):
                    return True
            sub_s += i
        return False
