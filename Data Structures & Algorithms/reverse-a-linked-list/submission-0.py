# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Understand:
Input: head of a singly linked list
Output: head of the reversed linked list

Edge cases:
- Empty list
- One node

Match:
Use pointers.
We need to reverse each node’s next pointer without losing the rest of the list.

Plan:
- Set prev = None
- Set current = head
- While current exists:
    - Save current.next in next_node
    - Point current.next to prev
    - Move prev to current
    - Move current to next_node
- When current becomes None, prev is the new head
- Return prev

Implement:
prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

return prev

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next

            current.next = prev
            prev = current
            current = next_node

        return prev

"""
Time: O(n)
It is O(n) becasue each item in the list is visited once
Space: O(1)
It is O(1) because no new space was created neither did the size of the array grow
"""
        