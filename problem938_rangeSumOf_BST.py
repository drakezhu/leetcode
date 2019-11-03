# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        '''
        如果当前节点在范围之外，就尽可能收敛进范围。
        比如，如果当前节点比最小值小，那就只用遍历当前节点的右子树（因为左子树的值更小）
        '''
        counter = 0
        def dfs(root, L, R, counter):
            if root is None:
                return counter
            if root.val < L:
                counter = dfs(root.right,L,R,counter)
            elif root.val > R:
                counter = dfs(root.left,L,R,counter)
            else:
                counter += root.val
                counter = dfs(root.left,L,R,counter)
                counter = dfs(root.right,L,R,counter)
            return counter
            
        counter = dfs(root,L,R,counter)
        
        
        
        return counter