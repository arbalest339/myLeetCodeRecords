class Solution:
    def findNthDigit(self, n: int) -> int:
        if not n:
            return 0
        place = 0
        prefixNum = 1
        while n > prefixNum-1:
            n -= prefixNum
            place += 1
            prefixNum = place*((10 ** place)*9//10)

        nth = n // place + 10**(place-1)
        digit = int(str(nth)[n % place])

        return digit


if __name__ == "__main__":
    solution = Solution()
    n = 190
    solution.findNthDigit(n)
