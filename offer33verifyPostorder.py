class Solution:
    def verifyPostorder(self, postorder):
        if len(postorder) <= 2:
            return True
        i = len(postorder)-1
        while i >= 0 and postorder[i] >= postorder[-1]:
            i -= 1
        j = 0
        while j < len(postorder) and postorder[j] < postorder[-1]:
            j += 1

        if i == j-1:
            return self.verifyPostorder(postorder[:j]) and self.verifyPostorder(postorder[j:-1])
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    postorder = [5, 4, 3, 2, 1]
    print(solution.verifyPostorder(postorder))
