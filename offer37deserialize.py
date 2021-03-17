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

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        import collections
        if not root:
            return []
        queue = [collections.deque(), collections.deque()]
        queue[0].append(root)

        res = [[]]
        level = 0
        while queue[0] or queue[1]:
            if not queue[level%2]:
                res.append([])
                level+=1
                ctn = False
                for item in queue[level%2]:
                    if item.val != None:
                        ctn = True
                if not ctn:
                    break

            cur = queue[level%2].popleft()
            res[level].append(cur.val)
            if cur.left:
                queue[(level+1)%2].append(cur.left)
            elif cur.val != None:
                queue[(level+1)%2].append(TreeNode(None))
            if cur.right:
                queue[(level+1)%2].append(cur.right)
            elif cur.val != None:
                queue[(level+1)%2].append(TreeNode(None))
        
        for i in range(1, len(res)):
            res[0] += res[i]
        return res[0]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        import collections
        queue = collections.deque()
        root = None
        i = 0
        while i<len(data):
            if queue:
                father = queue.popleft()
                left = TreeNode(data[i]) if data[i] != None else data[i]
                i += 1
                right = TreeNode(data[i]) if data[i] != None else data[i]
                father.left = left
                father.right = right
                i += 1
                if left != None:
                    queue.append(left)
                if right != None:
                    queue.append(right)
            else:
                root = TreeNode(data[i])
                queue.append(root)
                i += 1
        
        return root


if __name__ == "__main__":
    solution = Codec()
    preorder = [0,2,1,5,1,4,3,6,-1,8]
    inorder = [5,1,1,2,0,3,6,4,-1,8]
    root = TreeNode.buildTree(preorder, inorder)
    solution.deserialize(solution.serialize(root))
#       0
#     2   4
#   1    3 -1
#  5 1    6  8 