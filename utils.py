class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def buildTree(treeList):
        if not treeList:
            return None
        import collections
        queue = collections.deque()
        root = TreeNode(treeList[0])
        queue.append(root)
        i = 1
        while i < len(treeList):
            cur = queue.popleft()
            if treeList[i]:
                cur.left = TreeNode(treeList[i])
                queue.append(cur.left)
            i += 1
            if treeList[i]:
                cur.right = TreeNode(treeList[i])
                queue.append(cur.right)
            i += 1
        return root

    @staticmethod
    def buildTreeWithOrder(preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1:]

        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1:]

        root.left = TreeNode.buildTree(left_preorder, left_inorder)
        root.right = TreeNode.buildTree(right_preorder, right_inorder)

        return root
