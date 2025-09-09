# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def _util(node):
            if not node:
                return 0
            
            left = _util(node.left)
            right = _util(node.right)
            return 1 + max(left, right)
        
        return _util(root)

        