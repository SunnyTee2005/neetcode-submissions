# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = list1
        a2 = list2
        ans = ListNode
        ans_t = ans
        while a1 != None and a2 != None :
            if a1.val <= a2.val :
                t = a1.next
                ans_t.next = a1
                a1 = t
            else :
                t = a2.next
                ans_t.next = a2
                a2 = t
            ans_t = ans_t.next

        if a1 != None :
            ans_t.next = a1
        else : ans_t.next = a2
    
        return ans.next


        