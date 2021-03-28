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
            if i< len(treelist) and treeList[i]:
                cur.right = TreeNode(treeList[i])
                queue.append(cur.right)
            i += 1
        return root


class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.

    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     import collections
    #     if not root:
    #         return []
    #     queue = [collections.deque(), collections.deque()]
    #     queue[0].append(root)

    #     res = [[]]
    #     level = 0
    #     while queue[0] or queue[1]:
    #         if not queue[level % 2]:
    #             res.append([])
    #             level += 1
    #             ctn = False
    #             for item in queue[level % 2]:
    #                 if item.val != None:
    #                     ctn = True
    #             if not ctn:
    #                 break

    #         cur = queue[level % 2].popleft()
    #         res[level].append(cur.val)
    #         if cur.left:
    #             queue[(level+1) % 2].append(cur.left)
    #         elif cur.val != None:
    #             queue[(level+1) % 2].append(TreeNode(None))
    #         if cur.right:
    #             queue[(level+1) % 2].append(cur.right)
    #         elif cur.val != None:
    #             queue[(level+1) % 2].append(TreeNode(None))

    #     for i in range(1, len(res)):
    #         res[0] += res[i]
    #     return res[0]

    # def deserialize(self, data):
        # """Decodes your encoded data to tree.

        # :type data: str
        # :rtype: TreeNode
        # """
        # import collections
        # queue = collections.deque()
        # root = None
        # i = 0
        # while i < len(data):
        #     if queue:
        #         father = queue.popleft()
        #         left = TreeNode(data[i]) if data[i] != None else data[i]
        #         i += 1
        #         right = TreeNode(data[i]) if data[i] != None else data[i]
        #         father.left = left
        #         father.right = right
        #         i += 1
        #         if left != None:
        #             queue.append(left)
        #         if right != None:
        #             queue.append(right)
        #     else:
        #         root = TreeNode(data[i])
        #         queue.append(root)
        #         i += 1

        # return root
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        from collections import deque
        res = []
        queue = [deque(), deque()]
        level = 0
        queue[level].append(root)
        thislevel = []
        while queue[0] or queue[1]:
            if not queue[level%2]:
                level += 1
                app = False
                for v in thislevel:
                    if v != None:
                        app = True
                if app: 
                    res += thislevel
                    thislevel = []
            else:
                cur = queue[level%2].popleft()
                if cur:
                    thislevel.append(cur.val)
                else:
                    thislevel.append(None)
                    continue

                if cur.left:
                    queue[(level+1)%2].append(cur.left)
                else:
                    queue[(level+1)%2].append(None)
                if cur.right:
                    queue[(level+1)%2].append(cur.right)
                else:
                    queue[(level+1)%2].append(None)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        import collections
        queue = collections.deque()
        root = TreeNode(data[0])
        queue.append(root)
        i = 1
        while i < len(data):
            cur = queue.popleft()
            if data[i] != None:
                cur.left = TreeNode(data[i])
                queue.append(cur.left)
            i += 1
            if i< len(data) and data[i] != None:
                cur.right = TreeNode(data[i])
                queue.append(cur.right)
            i += 1
        return root


if __name__ == "__main__":
    solution = Codec()
    treelist = [10,9,11,8,None,None,12,7,None,None,13,6,None,None,14,5,None,None,15,4,None,None,16,3,None,None,17,2,None,None,18,1,None,None,19,0]
    root = TreeNode.buildTree(treelist)
    solution.deserialize(solution.serialize(root))
#       0
#     2   4
#   1    3 -1
#  5 1    6  8
