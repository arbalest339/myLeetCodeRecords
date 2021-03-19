class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def buildTree(preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
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


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:  # 中序遍历换皮
        if not root:
            return True
        treeStack = [root]
        inorder = []
        while treeStack:
            cur_node = treeStack.pop()
            if cur_node:
                if cur_node.right:
                    treeStack.append(cur_node.right)
                treeStack.append(cur_node)
                treeStack.append(None)
                if cur_node.left:
                    treeStack.append(cur_node.left)
            else:
                inorder.append(treeStack.pop())

        for i, val in enumerate(inorder):
            if inorder[i].val != inorder[-i-1].val:
                return False
            if inorder[i].right and not inorder[-i-1].left:
                return False
            elif inorder[i].right and inorder[-i-1].left and inorder[i].right.val != inorder[-i-1].left.val:
                return False
            if inorder[i].left and not inorder[-i-1].right:
                return False
            elif inorder[i].left and inorder[-i-1].right and inorder[i].left.val != inorder[-i-1].right.val:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    preorder = [1, 2, 3, 4, 2, 4, 3]
    inorder = [3, 2, 4, 1, 4, 2, 3]
    root = TreeNode.buildTree(preorder, inorder)
    print(solution.isSymmetric(root))
#      1
#   2     2
#  3  4  4  3
#   2      2
