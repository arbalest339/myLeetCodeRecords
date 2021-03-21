class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def buildTree(treeList, p, q):
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
            if treeList[i] == p:
                p = cur.left
            if treeList[i] == q:
                q = cur.left

            i += 1
            if treeList[i] != None:
                cur.right = TreeNode(treeList[i])
                queue.append(cur.right)
            if treeList[i] == p:
                p = cur.right
            if treeList[i] == q:
                q = cur.right
            i += 1
        return root, p, q


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        isself = None
        if root == p or root == q:
            isself = True

        if root.left:
            inleft = self.lowestCommonAncestor(root.left, p, q)
        else:
            inleft = None
        if root.right:
            inright = self.lowestCommonAncestor(root.right, p, q)
        else:
            inright = None
        
        if inleft==True and inright==True or ((inleft==True or inright==True) and isself):
            return root
        elif inleft:
            return inleft
        elif inright:
            return inright
        else:
            return isself


if __name__ == "__main__":
    solution = Solution()
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 2
    root, p, q = TreeNode.buildTree(root, p, q)
    solution.lowestCommonAncestor(root, p, q)
