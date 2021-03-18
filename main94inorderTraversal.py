class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                cur = stack.pop()
                res.append(cur.val)
                continue
            if cur.right:
                stack.append(cur.right)
            stack.append(cur)
            stack.append(None)
            if cur.left:
                stack.append(cur.left)
        return res

    def MorrisInorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                predecessor = cur.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right  # 指向最右
                if not predecessor.right:   # 左子树的最右的后续连接到根
                    predecessor.right = cur
                    cur = cur.left
                else:   # 左子树访问完成
                    res.append(root.val)
                    predecessor.right = None
                    cur = cur.right

        return res
