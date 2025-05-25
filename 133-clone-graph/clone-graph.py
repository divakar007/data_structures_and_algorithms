"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        newNodes = {}
        dq = deque([])
        dq.append(node)

        newNodes[node] = Node(node.val)
        while dq:
            curr = dq.popleft()
            for nei in curr.neighbors:
                if nei not in newNodes:
                    newNodes[nei] = Node(nei.val, None)
                    dq.append(nei)
                newNodes[curr].neighbors.append(newNodes[nei])
            
        return newNodes[node]

            

        