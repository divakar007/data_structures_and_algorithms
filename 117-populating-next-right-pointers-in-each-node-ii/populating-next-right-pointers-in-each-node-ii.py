"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        que = deque([(root, 0)])
        while que:
            node, level = que.popleft()

            if que and level == que[0][1]:
                node.next = que[0][0]
            
            if node.left:
                que.append((node.left, level + 1))
            if node.right:
                que.append((node.right, level + 1))
        
        return root
            


        