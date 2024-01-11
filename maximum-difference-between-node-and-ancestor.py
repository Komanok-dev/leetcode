from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, 0, float('inf'))]
        while stack:
            node, maximum, minimum = stack.pop()
            if not node:
                continue
            result = max(result, maximum - node.val, node.val - minimum)
            maximum = max(maximum, node.val)
            minimum = min(minimum, node.val)
            stack.append((node.left, maximum, minimum))
            stack.append((node.right, maximum, minimum))
        return result
