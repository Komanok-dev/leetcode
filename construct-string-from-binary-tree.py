from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []

        def preoder(root):
            if not root:
                return
            result.append('(')
            result.append(str(root.val))
            if not root.left and root.right:
                result.append('()')
            preoder(root.left)
            preoder(root.right)
            result.append(')')

        preoder(root)
        return ''.join(result)[1:-1]
