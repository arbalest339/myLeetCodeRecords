
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):   # 不匹配字符，将该组合扔掉，不再进行匹配。
                        f[i][j] |= f[i - 1][j]  # 匹配 s 末尾的一个字符，将该字符扔掉，而该组合还可以继续进行匹配
                else:   # 如果 p 的第 j 个字符是一个小写字母，那么我们必须在 s 中匹配一个相同的小写字母
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


if __name__ == "__main__":
    solution = Solution()
    s = "aabb"
    p = "a*b*."
    print(solution.isMatch(s, p))
