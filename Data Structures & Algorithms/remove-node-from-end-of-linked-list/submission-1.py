# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        # use 2 pointers, when r is null then break and set the l current node

        # to point at the next next one

        # [1,2,3,4]
        # n = 2

        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -=1

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next
        


        
        


        