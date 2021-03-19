class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m = len(text1)+1
        n = len(text2)+1
        dp = [[0]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[m-1][n-1]


if __name__ == "__main__":
    solution = Solution()
    text1 = "abcde"
    text2 = "ace"
    solution.longestCommonSubsequence(text1, text2)
