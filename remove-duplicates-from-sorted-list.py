from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new_list = tail = ListNode(head.val)
        node = head
        while node:
            if node.next:
                if node.next.val != node.val:
                    tail.next = node.next
                    tail = tail.next
            else:
                tail.next = None
            node = node.next
        return new_list
