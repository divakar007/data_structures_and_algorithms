# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_path_sum = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            
            if node.left == None and node.right == None:
                self.max_path_sum = max(self.max_path_sum, node.val)
                return node.val
            
            left = right = 0
            if node.left:
                left = helper(node.left)
            if node.right:
                right = helper(node.right)
                        
            self.max_path_sum = max([self.max_path_sum, left + right + node.val, node.val, node.val + left, node.val + right])

            return node.val + max(left, right, 0)
        
        helper(root)
        return self.max_path_sum
        