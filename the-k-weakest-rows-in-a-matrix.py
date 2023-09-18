class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        ans = {}
        for i in range(len(mat)):
            ans[i] = mat[i].count(1)
        ans = dict(sorted(ans.items(), key=lambda x: x[1]))
        return list(ans.keys())[:k]
