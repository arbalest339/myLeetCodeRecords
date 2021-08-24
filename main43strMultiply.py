class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(n) for n in num1]
        num2 = [int(n) for n in num2]
        multi = 0
        for n1 in range(1, len(num1)+1):
            for n2 in range(1, len(num2)+1):
                multi += num1[-n1]*num2[-n2]*pow(10, n1-1)*pow(10, n2-1)
        return str(multi)


if __name__ == "__main__":
    solution = Solution()
    num1 = "123"
    num2 = "456"
    print(solution.multiply(num1, num2))
