from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def create_list(vals):
            new_list = ListNode()
            tail = new_list
            for i in range(len(vals)):
                tail.next = ListNode(vals[i])
                tail = tail.next
            return new_list.next

        node = head
        vals = []

        while node:
            vals.append(node.val)
            node = node.next

        ans = []
        start = 0
        step = len(vals) // k if len(vals) // k > 0 else 1

        if len(vals) <= k:
            end = 1
            step = 1
            remainder = 0
        else:
            remainder = len(vals) % k
            end = len(vals) // k + (1 if remainder else 0)

        while k > 0:
            remainder -= 1
            ans.append(create_list(vals[start:end]))
            start = end
            end += step + (1 if remainder > 0 else 0)
            k -= 1

        return ans
