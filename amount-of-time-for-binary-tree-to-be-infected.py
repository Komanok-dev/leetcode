from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(curr, start, result):
            if curr is None:
                return [-1, -1]
            left = dfs(curr.left, start, result)
            right = dfs(curr.right, start, result)
            d = -1
            if curr.val == start:
                d = 0
                result[0] = max(left[0], right[0]) + 1
            elif left[1] >= 0:
                d = left[1] + 1
                result[0] = max(result[0], right[0] + 1 + d)
            elif right[1] >= 0:
                d = right[1] + 1
                result[0] = max(result[0], left[0] + 1 + d)
            return [max(left[0], right[0]) + 1, d]
        result = [-1]
        dfs(root, start, result)
        return result[0]
