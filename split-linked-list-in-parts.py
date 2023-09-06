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




head = [1,2,3,4,5,6,7,8,9,10]
k = 3
head = [1,2,3]
k = 5
head = [0,1,2] # [[0,1],[2]]
k = 2
head = [0,1,2,3,4] # [[0,1],[2,3],[4]]
k = 3

linked_list = ListNode(head[0])
tail = linked_list
for i in range(1, len(head)):
    tail.next = ListNode(head[i])
    tail = tail.next

node = linked_list
while node:
    print(node.val, end=' --> ')
    node = node.next
print('null\n')


a = Solution()
new = a.splitListToParts(linked_list, k)

for j in new:
    node = j
    while node:
        print(node.val, end=' --> ')
        node = node.next
    print('null')
