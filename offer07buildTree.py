# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:     # 方法二
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root


if __name__ == "__main__":
    preorder = [3, 9, 8, 5, 4, 10, 20, 15, 7]
    inorder = [4, 5, 8, 10, 9, 3, 15, 20, 7]

    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print(root)