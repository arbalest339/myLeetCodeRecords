class Solution:
    def myPow(self, x: float, n: int) -> float:
        def toBinary(n):
            binary = ""
            while n > 0:
                binary += str(n%2)
                n = n // 2
            return binary
        if n<0:
            x = 1 / x
            n = -n
        bn = toBinary(n)
        res = 1
        for b in bn:
            if b == "1":
                res = res * x
            x = x * x
        return res
        

if __name__ == "__main__":
    solution = Solution()
    x = 2
    n = -2
    print(solution.myPow(x, n))
    limit = 10 ** 2
    print(list(range(1, limit)))
