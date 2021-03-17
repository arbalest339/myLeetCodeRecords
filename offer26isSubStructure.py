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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False
        treeStack = [A]
        while treeStack:
            root = treeStack.pop()
            if root.val == B.val:
                subTreeStackA = [root]
                subTreeStackB = [B]
                while subTreeStackA and subTreeStackB:
                    rootA = subTreeStackA.pop()
                    rootB = subTreeStackB.pop()
                    if rootA.val != rootB.val:
                        break
                    if rootB.right:
                        if rootA.right:
                            subTreeStackA.append(rootA.right)
                            subTreeStackB.append(rootB.right)
                        else:
                            break
                    if rootB.left:
                        if rootA.left:
                            subTreeStackA.append(rootA.left)
                            subTreeStackB.append(rootB.left)
                        else:
                            break
                    if not subTreeStackB:
                        return True

            if root.right:
                treeStack.append(root.right)
            if root.left:
                treeStack.append(root.left)
        
        return False


if __name__ == "__main__":
    solution = Solution()
    preorder = [3, 4, 1, 2, 5]
    inorder = [1, 4, 2, 3, 5]
    A = TreeNode.buildTree(preorder, inorder)
    preorder = [4, 1]
    inorder = [1, 4]
    B = TreeNode.buildTree(preorder, inorder)
    solution.isSubStructure(A, B)
