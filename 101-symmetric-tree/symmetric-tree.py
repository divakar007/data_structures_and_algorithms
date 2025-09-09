# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        def util(left, right):
            if left == None and right == None:
                return True
            
            if not (left and right):
                return False
            
            if left.val == right.val:
                return util(left.left, right.right) and util(left.right, right.left)
            
            return False

        if root.left == None and root.right == None:
            return True
            
        if not (root.left and root.right):
            return False
        
        return util(root.left, root.right)
        
        
        

