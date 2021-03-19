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
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        stack = [[root], []]
        res = []
        level = 0
        while stack[0] or stack[1]:
            cur = stack[level % 2].pop()
            if cur.right:
                stack[(level+1) % 2].append(cur.right)
            if cur.left:
                stack[(level+1) % 2].append(cur.left)

            if not stack[level % 2]:
                level += 1

        return level


if __name__ == "__main__":
    solution = Solution()
    treeList = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.buildTree(treeList)
    solution.maxDepth(root)
