class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "#" + word1
        word2 = "#" + word2
        m = len(word1)
        n = len(word2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j

        for i in range(1, m):   # 三种操作转化为，删除A的一个字符、删除B的一个字符，改变A的一个字符
            for j in range(1, n):
                if word1[i] != word2[j]:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[m-1][n-1]


if __name__ == "__main__":
    solution = Solution()
    text1 = "zoologicoarchaeologist"
    text2 = "zoogeologist"
    solution.minDistance(text1, text2)
