from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time Complexity O(n+m)
    # Space Complexity O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA

    # Time Complexity O(n+m)
    # Space Complexity O(n)
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeB = headB
        lstB = []
        while nodeB:
            lstB.append(nodeB)
            nodeB = nodeB.next
        nodeA = headA
        while nodeA:
            if nodeA in lstB:
                return nodeA
            nodeA = nodeA.next
