class Solution:
    def countDigitOne(self, n: int) -> int:
        place = 0
        cur_remain = 0
        remain = []
        res = 0

        while n>0:
            thisPlace = n % 10
            n = n // 10

            if thisPlace == 0: # 若当前位是0，则本位上1的个数是: 前所有位
                res += n*10**place
            elif thisPlace ==1: # 若当前位是1，则本位上1的个数是: 前所有位*10 ** 本位+本位后几位的数
                res += n*10**place + cur_remain + 1
            elif thisPlace > 1: # 若当前位大于1，则本位上1的个数是: （前所有位+1）*10 ** 本位
                res += (n + 1)*10**place

            cur_remain += thisPlace*10**place
            place += 1
                
        return res


if __name__ == "__main__":
    solution = Solution()
    n = 12
    solution.countDigitOne(n)