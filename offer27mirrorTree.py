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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        treeStack = [root]
        while treeStack:
            cur_node = treeStack.pop()
            tmp = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = tmp

            if cur_node.right:
                treeStack.append(cur_node.right)
            if cur_node.left:
                treeStack.append(cur_node.left)
        
        return root


if __name__ == "__main__":
    solution = Solution()
    preorder = [4,2,1,3,7,6,9]
    inorder = [1,2,3,4,6,7,9]
    root = TreeNode.buildTree(preorder, inorder)
    solution.mirrorTree(root)