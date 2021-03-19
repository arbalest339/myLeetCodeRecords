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
    def kthLargest(self, root, k: int) -> int:
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if not cur:
                cur = stack.pop()
                res.append(cur.val)
            else:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)

        return res[-k]


if __name__ == "__main__":
    solution = Solution()
    treeList = [3, 1, 4, None, 2]
    k = 1
    root = TreeNode.buildTree(treeList)
    solution.kthLargest(root, k)
