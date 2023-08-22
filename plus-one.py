class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(1, len(digits)+1):
            if digits[-i] != 9:
                digits[-i] += 1
                break
            else:
                digits[-i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


    # Math
    def plusOne2(self, digits: list[int]) -> list[int]:
        number = 0
        for i in digits:
            number = number * 10 + i
        number += 1
        digits_plus_one = []
        while number != 0:
            digits_plus_one.append(number % 10)
            number //= 10
        return digits_plus_one[::-1]
