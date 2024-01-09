from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            result = []
            tree = [root]
            while tree:
                node = tree.pop()
                if node:
                    if not node.left and not node.right:
                        result.append(node.val)
                    else:
                        tree.append(node.right)
                        tree.append(node.left)
            return result
        return get_leaves(root1) == get_leaves(root2)
