from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        node = head
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next if node.next.next else None
            else:
                node = node.next
        return head
