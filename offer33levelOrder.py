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
    def levelOrder(self, root: TreeNode):
        import collections
        if not root:
            return []
        stack = [collections.deque(), collections.deque()]
        stack[0].append(root)

        res = [[]]
        level = 0
        while stack[0] or stack[1]:
            if not stack[level%2]:
                res.append([])
                level+=1

            cur = stack[level%2].pop()
            res[level].append(cur.val)
            if level%2==0:
                if cur.left:
                    stack[(level+1)%2].append(cur.left)
                if cur.right:
                    stack[(level+1)%2].append(cur.right)
            else:
                if cur.right:
                    stack[(level+1)%2].append(cur.right)
                if cur.left:
                    stack[(level+1)%2].append(cur.left)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    preorder = [0,2,1,5,1,4,3,6,-1,8]
    inorder = [5,1,1,2,0,3,6,4,-1,8]
    root = TreeNode.buildTree(preorder, inorder)
    print(solution.levelOrder(root))
      
#       0
#     2   4
#   1    3 -1
#  5 1    6  8 