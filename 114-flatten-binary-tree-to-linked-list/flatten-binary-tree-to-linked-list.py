# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return None
            left_tail  = helper(node.left)
            right_tail = helper(node.right)

            if left_tail:
                # splice: node.left chain goes to node.right
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # return the tail of the whole (flattened) subtree
            return right_tail or left_tail or node

        helper(root)