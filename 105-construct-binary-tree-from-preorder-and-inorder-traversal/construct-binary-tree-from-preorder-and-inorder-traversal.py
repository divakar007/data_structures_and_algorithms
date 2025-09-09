# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        center = inorder.index(preorder[0])
        left_inorder = inorder[:center]
        right_inorder = inorder[center+1:]

        left_n = len(left_inorder)

        root.left = self.buildTree(preorder[1:left_n+1], left_inorder)
        root.right = self.buildTree(preorder[left_n+1:], right_inorder)

        return root


