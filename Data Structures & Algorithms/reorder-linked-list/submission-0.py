# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # curr = head

        # tail?

        # dummy node

        # take the first node of the list, 
        # then move next,
        # take the last node of the list,
        # then move backwards?

        # could I maybe reverse the list as another list,

        # and then append it to a new dummy list

        # find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 1, s2, sec3 -> none, f4 

        second = slow.next
        prev = slow.next = None
        
        # reversing second portion of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2













