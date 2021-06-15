class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

res = 0

def postOrder(root, target1, target2):
    if not root:
        return

    if root.left:
        left = postOrder(root.left, target1, target2)
    if root.right:
        right = postOrder(root.right, target1, target2)

    if left == -1 and right == 1 or left == 1 and right == -1:
        res += root.val
        return 0
    elif left == -1:
        res += root.val
        if root.val == target2:
            return 0
        return -1
    elif right == 1:
        res += root.val
        if root.val == target1:
            return 0
        return 1

    if root.val == target1:
        res += root.val
        return -1
    elif root.val == target2:
        res += root.val
        return 1
    else:
        return 0
    

if __name__ == "__main__":
    root = TreeNode()
    postOrder(root, 2, 3)
    print(res)
