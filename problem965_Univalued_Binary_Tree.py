# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root.left:
            if root.left.val != root.val:
                return False
            else:
                if self.isUnivalTree(root.left) is False:
                    return False
        if root.right:
            if root.right.val != root.val:
                return False
            else:
                if self.isUnivalTree(root.right) is False:
                    return False
            
        
     
        
        return True
        