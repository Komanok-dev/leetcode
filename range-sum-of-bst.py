from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        bst = [root]
        while bst:
            node = bst.pop()
            if node:
                if low <= node.val <= high:
                    result += node.val
                if low < node.val:
                    bst.append(node.left)
                if high > node.val:
                    bst.append(node.right)
        return result
