class Solution(object):
    def delNodes(self, root, to_delete):
    
        def post_order(node, res):
            if node:
                #dfs
                post_order(node.left, res)
                post_order(node.right, res)
                                
                # 如果当前结点的左节点存在且在要删除的结点中，则另左节点为none
                if node.left and node.left.val in to_delete_set:
                    node.left = None
                    
                # 如果当前结点的右节点存在且在要删除的结点中，则另右节点为none
                if node.right and node.right.val in to_delete_set:
                    node.right = None
                    
                #如果当前结点是要删除的结点，则把左子树和右子树的根节点加入到返回list中
                if node.val in to_delete_set:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)
                
        res = []
        to_delete_set = set(to_delete)

        post_order(root, res)

        # 如果根节点不是要删除的结点，则将最后一个根节点的树返回； 如果根节点是要删除的结点，则在post_order中将会将其左右子树加入至返回list中
        if root.val not in to_delete_set:
            res.append(root)

        return res