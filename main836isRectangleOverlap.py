class Solution:  # 当证明 是 比较困难的时候 就证明 非否
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top


if __name__ == "__main__":
    solution = Solution()
    rec1 = [2, 17, 6, 20]
    rec2 = [3, 8, 6, 20]
    solution.isRectangleOverlap(rec1, rec2)
