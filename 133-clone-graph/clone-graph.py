from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        newNodes = {}
        dq = deque([node])
        newNodes[node] = Node(node.val)  # Create the first node

        while dq:
            curr = dq.popleft()
            for nei in curr.neighbors:
                if nei not in newNodes:
                    newNodes[nei] = Node(nei.val)
                    dq.append(nei)
                newNodes[curr].neighbors.append(newNodes[nei])

        return newNodes[node]
