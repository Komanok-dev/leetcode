from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        num1 = ''
        while node:
            num1 += str(node.val)
            node = node.next

        node = l2
        num2 = ''
        while node:
            num2 += str(node.val)
            node = node.next

        num = int(num1[::-1]) + int(num2[::-1])

        head = ListNode(num % 10)
        num //= 10
        tail = head
        while num > 0:
            tail.next = ListNode(num % 10)
            num //= 10
            tail = tail.next

        return head

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        node = head
        reminder = 0

        while l1 or l2:
            val = reminder
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            reminder, val = divmod(val, 10)
            node.next = ListNode(val)
            node = node.next

        if reminder == 1:
            node.next = ListNode(1)

        return head.next
