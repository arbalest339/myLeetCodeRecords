class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        elif num <26:
            return 2
        elif num <100:
            return 1
        if 9<num % 100<26:
            return self.translateNum(num // 10) + self.translateNum(num //100)
        else:
            return self.translateNum(num // 10)

if __name__ == "__main__":
    solution = Solution()
    n = 1727101694
    print(solution.translateNum(n))