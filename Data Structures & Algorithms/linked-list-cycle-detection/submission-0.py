# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()
        cycle = False
        ptr = head
        while ptr :
            if ptr in st :
                return True
            st.add(ptr)
            ptr = ptr.next
        return False
        