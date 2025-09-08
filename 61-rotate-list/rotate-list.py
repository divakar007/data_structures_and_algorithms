# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head:
            return head 
        
        n = 0
        temp = head
        while(temp):
            n += 1
            temp = temp.next 
        
        k = k % n

        if k == 0:
            return head
        temp = head
        ind = 0
        while(ind < n-k-1):
            temp = temp.next
            ind += 1
        
        new_head = temp.next
        temp.next = None

        temp = new_head
        while(temp.next != None):
            temp = temp.next
        
        temp.next = head

        return new_head

        