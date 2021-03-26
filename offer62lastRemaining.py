class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f
# 当长度为n时，删除的是 n%m个元素，之后长度变为n-1， m+1及以后的调整的前面
# 设n-1长度的序列留下了x， 则x在原本的位置为 m%n 之后的第 x个，即 (m%n+x)%n==(m+x)%n


if __name__ == "__main__":
    solution = Solution()
    n = 5
    m = 3
    solution.lastRemaining(n,m)