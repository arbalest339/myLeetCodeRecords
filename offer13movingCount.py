class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:   # k=9时与右、下联通，k=10时与右下联通
        def digitsum(n):
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return ans

        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)


if __name__ == "__main__":
    solution = Solution()
    m, n, k = 100,100,9
    print(solution.movingCount(m,n,k))
