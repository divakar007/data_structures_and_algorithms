# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        if root == None:
            return 0
        def helper(node, curr):
            if node.left == None and node.right == None:
                res.append(curr + str(node.val))
            if node.left:
                helper(node.left, curr + str(node.val))
            if node.right:
                helper(node.right, curr + str(node.val))

        helper(root, "")

        return sum([int(x) for x in res]) 


        

        