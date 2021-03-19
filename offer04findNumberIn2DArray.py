class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        # 查找失败的终点
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False

        if n >= m:
            # 分块部分的算法
            for i in range(m):  # 先判断一个正方形的部分
                if matrix[i][i] == target:    # 与对角线上元素对比
                    return True
                elif matrix[i][i] > target:   # 找到分水岭，将矩阵划为4块， 左上区域均比目标小，右下区域均比目标大
                    subMatrix1 = [matrix[j][i:m]
                                  for j in range(0, i)]   # 右上区域可能包含答案
                    subMatrix2 = [matrix[j][0:i]
                                  for j in range(i, n)]   # 左下区域可能包含答案
                    # 递归查找
                    return self.findNumberIn2DArray(subMatrix1, target) or self.findNumberIn2DArray(subMatrix2, target)

            for i in range(m, n):      # 下区使用线性查找法 反而能减少实际递归深度
                if matrix[i][m-1] == target:
                    return True
                elif matrix[i][m-1] > target:
                    for j in range(m):
                        if matrix[i][j] == target:
                            return True
            # 当对角线的最后一个元素也小于目标，答案在非正方形区域(下区)
            # subMatrix = [matrix[j]for j in range(m, n)]
            # return self.findNumberIn2DArray(subMatrix, target)

        else:
            for i in range(n):
                if matrix[i][i] == target:
                    return True
                elif matrix[i][i] > target:
                    subMatrix1 = [matrix[j][i:m] for j in range(0, i)]
                    subMatrix2 = [matrix[j][0:i] for j in range(i, n)]
                    return self.findNumberIn2DArray(subMatrix1, target) or self.findNumberIn2DArray(subMatrix2, target)

            for i in range(n, m):
                if matrix[n-1][i] == target:
                    return True
                elif matrix[n-1][i] > target:
                    for j in range(n):
                        if matrix[j][i] == target:
                            return True
            # subMatrix = [matrix[j][n:m]for j in range(0, n)]
            # return self.findNumberIn2DArray(subMatrix, target)

        return False


if __name__ == "__main__":
    input = [[4, 7, 11, 12, 16, 21, 23, 26],
             [5, 12, 17, 17, 18, 23, 26, 31],
             [8, 15, 21, 25, 26, 29, 33, 34],
             [13, 20, 26, 26, 29, 34, 39, 40],
             [18, 21, 31, 36, 41, 42, 42, 44],
             [19, 23, 31, 39, 46, 49, 50, 53],
             [23, 25, 33, 40, 50, 51, 55, 60],
             [27, 28, 33, 44, 51, 56, 61, 65],
             [32, 35, 39, 45, 54, 56, 65, 68],
             [33, 38, 40, 49, 56, 57, 66, 71]]
    target = 51
    solution = Solution()
    print(solution.findNumberIn2DArray(input, target))
