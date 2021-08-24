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
            if treeList[i] != None:
                cur.left = TreeNode(treeList[i])
                queue.append(cur.left)
            i += 1
            if i < len(treeList) and treeList[i]:
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

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        # if targetSum > 0 and root.val > targetSum:
        #     return False
        # if targetSum < 0 and root.val < targetSum:
        #     return False

        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val
        left, right = False, False
        if root.left:
            left = self.hasPathSum(root.left, targetSum)
        if root.right:
            right = self.hasPathSum(root.right, targetSum)
        
        return left or right
    
if __name__ == "__main__":
    solution = Solution()
    nodeList = [8,9,-6,None,None,5,9]
    target = 7
    root = TreeNode.buildTree(nodeList)
    print(solution.hasPathSum(root, target))