# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head_copy = head

        seen = set()

        while head_copy:
            if head_copy in seen:
                return True

            seen.add(head_copy)
            head_copy = head_copy.next
            
        return False 