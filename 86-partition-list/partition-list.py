# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        left = head
        prev = ListNode(-10000)
        prev.next = left
        nxt = head.next
        right = head
        res = prev

        while(left):
            if left.val >= x:
                break
            prev = left
            left = nxt
            if left:
                nxt = left.next
        
        if not left:
            return res.next

        right = left.next
        right_prev = left
        if right:
            right_nxt = right.next
        while (right):
            if (right.val < x):
                right_prev.next = right_nxt
                right.next = left
                prev.next = right
                prev = right
                right = right_prev.next
                if right:
                    right_nxt = right.next
            else:
                right_prev = right
                right = right_nxt
                if right:
                    right_nxt = right.next

        
        return res.next
            


                
            

        