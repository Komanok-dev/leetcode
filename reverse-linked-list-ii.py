from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(lst: Optional[ListNode]) -> Optional[ListNode]:
            node = lst
            prev = curr = None
            while node:
                curr = node.next
                node.next = prev
                prev = node
                node = curr
            lst = prev
            return lst

        if left == right:
            return head
        
        # split first part
        tail = head
        if left > 1:
            counter = left - 1
            while counter > 1:
                tail = tail.next
                counter -= 1
            head2 = tail.next
            tail.next = None
        else:
            head2 = head
            tail = None

        # extract part and reverse
        counter = right - left + 1
        tail2 = head2

        while counter > 1 and tail2.next:
            tail2 = tail2.next
            counter -= 1

        head3 = tail2.next
        tail2.next = None
        head2 = reverseList(head2)

        # merge parts
        if tail:
            tail.next = tail2
        else:
            tail = head = head2

        while tail and tail.next:
            tail = tail.next
        tail.next = head3

        return head
