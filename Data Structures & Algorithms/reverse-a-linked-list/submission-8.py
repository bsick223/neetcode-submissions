# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr, prev = head, None

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        
















        # def reverse(curr, prev):

        #     if not curr:
        #         return prev

        #     else:
        #         nxt = curr.next
        #         curr.next = prev
        #         return reverse(nxt, curr)

        # return reverse(head, None)
