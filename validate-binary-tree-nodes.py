class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        roots = set(range(n)) - set(leftChild) - set(rightChild)
        if len(roots) != 1:
            return False
        root, = roots
        stk = [root]
        lookup = set([root])
        while stk:
            node = stk.pop()
            for c in (leftChild[node], rightChild[node]):
                if c < 0:
                    continue
                if c in lookup:
                    return False
                lookup.add(c)
                stk.append(c)
        return len(lookup) == n
