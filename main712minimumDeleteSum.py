class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1:
            res = 0
            for c in s2:
                res += ord(c)
            return 0
        if not s2:
            res = 0
            for c in s1:
                res += ord(c)
            return 0
        s1 = "#"+s1
        s2 = "#"+s2
        dp = [[0]*len(s2) for _ in range(len(s1))]
        for i in range(1, len(s1)):
            dp[i][0] = ord(s1[i]) + dp[i-1][0]
        for i in range(1, len(s2)):
            dp[0][i] = ord(s2[i]) + dp[0][i-1]

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] != s2[j]:
                    dp[i][j] = min(ord(s1[i])+dp[i-1][j],
                                   ord(s2[j])+dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    # s1, s2 = "sea", "eat"
    s1, s2 = "delete", "leet"
    solution.minimumDeleteSum(s1, s2)
