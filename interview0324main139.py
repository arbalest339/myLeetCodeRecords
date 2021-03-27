class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n=len(s)    # 动态规划问题
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    s = "goalspecial"
    wordDict = ["go","goal","goals","special"]
    print(solution.wordBreak(s, wordDict))