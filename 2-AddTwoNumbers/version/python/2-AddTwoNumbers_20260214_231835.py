# Last updated: 2/14/2026, 11:18:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        dummy = ListNode()
10        cur = dummy
11
12        carry = 0
13        while l1 or l2 or carry:
14            v1 = l1.val if l1 else 0
15            v2 = l2.val if l2 else 0
16
17            # new digit
18            val = v1 + v2 + carry
19            carry = val // 10
20            val = val % 10
21            cur.next = ListNode(val)
22
23            # update ptrs
24            cur = cur.next
25            l1 = l1.next if l1 else None
26            l2 = l2.next if l2 else None
27
28        return dummy.next