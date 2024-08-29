class Solution:
    def countSeniors(self, details: list[str]) -> int:
        result = 0
        for detail in details:
            if int(detail[11]) * 10 + int(detail[12]) > 60:
                result += 1
        return result
