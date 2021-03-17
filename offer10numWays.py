class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            while n > 1:
                a, b = b, a+b
                n -= 1
            return b % 1000000007

# 当直接求得答案比较困难时，应该想到从上一个状态递推


if __name__ == "__main__":
    n = 78
    solution = Solution()
    print(solution.numWays(n))