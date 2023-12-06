class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        sum_weeks = 28 * weeks + (((weeks - 1) * weeks) // 2) * 7
        days = n % 7
        sum_days = (days * (days + 1)) // 2 + days * weeks
        return sum_days + sum_weeks
