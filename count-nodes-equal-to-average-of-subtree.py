# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0]*3
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[0]+right[0]+node.val,
                    left[1]+right[1]+1,
                    left[2]+right[2]+int((left[0]+right[0]+node.val)//(left[1]+right[1]+1) == node.val)]
        
        return dfs(root)[2]
