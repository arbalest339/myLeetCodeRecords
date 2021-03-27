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
    def pathSum(self, root, targetSum: int):
        if not root:
            return []
        stack = [[root, [], targetSum]]
        res = []
        while stack:
            cur, path, target = stack.pop()
            if not cur.left and not cur.right:
                if cur.val == target:
                    path.append(cur.val)
                    res.append(path)
            
            else:
                # if cur.val > target:
                #     continue
                target -= cur.val
                path.append(cur.val)
                if cur.right:
                    stack.append([cur.right, path.copy(), target])
                if cur.left:
                    stack.append([cur.left, path.copy(), target])
        
        return res

if __name__ == "__main__":
    treelist = [-2,None, -3]
    targetSum = -5
    root = TreeNode.buildTree(treelist)
    solution = Solution()
    solution.pathSum(root, targetSum)