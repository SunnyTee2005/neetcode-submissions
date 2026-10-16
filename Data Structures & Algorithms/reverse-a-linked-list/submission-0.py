# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # list length 0 or 1
        if head == None or head.next == None :
            return head
        a = head
        b = head.next
        head.next = None
        while b != None :
            tmp = b.next
            b.next = a
            a = b
            b = tmp
        head = a
        return head

        