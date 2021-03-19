class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0  # a,b,c分别是三个指针，指向当前*2，*3，*5之后有可能是最小的上一个丑数
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)     # 只需要找到*2 *3 *5之后最小的一个数就行
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    n = 10
    solution.nthUglyNumber(n)
