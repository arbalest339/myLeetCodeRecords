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
            i += 1
            if treeList[i] != None:
                cur.right = TreeNode(treeList[i])
                queue.append(cur.right)
            if cur.val == p:
                p = cur
            if cur.val == q:
                q = cur
            i += 1
        return root, p, q


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val: # 搜索树中，可以判断目标节点在左还是右
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor


if __name__ == "__main__":
    solution = Solution()
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 8
    root, p, q = TreeNode.buildTree(root,p,q)
    solution.lowestCommonAncestor(root, p, q)
