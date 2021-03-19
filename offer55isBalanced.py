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


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depthBalance(root)[0]

    def depthBalance(self, root) -> int:
        if not root:
            return True, 0
        if not root.left and not root.right:
            return True, 1
        else:
            leftBal, leftDepth = self.depthBalance(root.left)
            rightBal, rightDepth = self.depthBalance(root.right)
            if not leftBal or not rightBal:
                return False, 0
            else:
                if not -2 < leftDepth-rightDepth < 2:
                    return False, 0
                else:
                    return True, max(leftDepth, rightDepth)+1


if __name__ == "__main__":
    solution = Solution()
    treeList = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = TreeNode.buildTree(treeList)
    solution.isBalanced(root)
