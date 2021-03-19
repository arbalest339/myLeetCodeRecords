class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        level, m, n = 0, len(matrix), len(matrix[0])
        while level*2 < min(m, n):
            for j in range(level, n-level):
                res.append(matrix[level][j])
            if level*2+2 <= m:
                for i in range(level+1, m-level):
                    res.append(matrix[i][n-level-1])
                if level*2+2 <= n:
                    for j in range(n-level-2, level-1, -1):
                        res.append(matrix[m-level-1][j])
                    for i in range(m-level-2, level, -1):
                        res.append(matrix[i][level])
            level += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    matrix = [[2, 5, 8],
              [4, 0, -1]]
    print(solution.spiralOrder(matrix))
