from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Space Complexity O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'checked node':
                return True
            head.val = 'checked node'
            head = head.next
        return False

    # Fast
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        tail = head
        while tail and tail.next:
            head = head.next
            tail = tail.next.next
            if tail is head:
                return True
        return False

    # Slow
    def hasCycle3(self, head: Optional[ListNode]) -> bool:
        cache = []
        while head:
            if head in cache:
                return True
            cache.append(head)
            head = head.next
        return False
