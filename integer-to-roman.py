class Solution:
    ROMANS = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    
    def intToRoman(self, num: int) -> str:
        ans = []
        div = 1
        while num > 0:
            digit = num % 10
            if self.ROMANS.get(digit*div) is None:
                if digit < 5:
                    ans.append(self.ROMANS.get(1*div) * digit)
                else:
                    ans.append(self.ROMANS.get(5*div) + self.ROMANS.get(1*div) * (digit - 5))
            else:
                ans.append(self.ROMANS.get(digit*div))
            num //= 10
            div *= 10
        return ''.join(reversed(ans))
