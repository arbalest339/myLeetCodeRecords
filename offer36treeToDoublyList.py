class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def buildTree(preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Node
        """
        if not preorder:
            return None

        root = Node(preorder[0])
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1:]

        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1:]

        root.left = Node.buildTree(left_preorder, left_inorder)
        root.right = Node.buildTree(right_preorder, right_inorder)

        return root


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None
        treeStack = [root]
        inorder = []
        while treeStack:
            cur_node = treeStack.pop()
            if cur_node:
                if cur_node.right:
                    treeStack.append(cur_node.right)
                treeStack.append(cur_node)
                treeStack.append(None)
                if cur_node.left:
                    treeStack.append(cur_node.left)
            else:
                inorder.append(treeStack.pop())
        
        for i in range(len(inorder)):
            inorder[i].left = inorder[i-1]
            inorder[i].right = inorder[(i+1)%len(inorder)]
        
        return inorder[0]


if __name__ == "__main__":
    solution = Solution()
    preorder = [4,2,1,3,6,5,7]
    inorder = [1,2,3,4,5,6,7]
    root = Node.buildTree(preorder, inorder)
    print(solution.treeToDoublyList(root))