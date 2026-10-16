# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ls = []
        p = head
        while p :
            ls.append(p)
            p = p.next
        #print(ls)
        mid = len(ls) // 2
        n = len(ls)
        i = 1
        if n % 2 :
            while i <= mid :
                # front
                ls[ i - 1 ].next = ls[ n - i ]
                ls[ n - i ].next = ls[i]
                ls[ n - i - 1].next = None
                i += 1
        else :
            while i < mid :
                # front
                ls[ i - 1 ].next = ls[ n - i ]
                ls[ n - i ].next = ls[i]
                ls[ n - i - 1].next = None
                i += 1
        
        

        