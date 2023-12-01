class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result, curr = [], 1
        for t in target:
            result.extend(["Push", "Pop"] * (t-curr))
            result.append("Push")
            curr = t + 1
        return result
