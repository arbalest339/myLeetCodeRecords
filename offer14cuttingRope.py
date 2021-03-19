class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        max_multi = 0
        for i in range(2, 4):   # 数学推导可得实质上3为大多数情况下的分割点
            exp = n // i
            remain = n % i
            if remain == 0:
                cur_max = i**exp
            elif remain == 1:
                cur_max = i**(exp-1)*(i+1)
            else:
                cur_max = i**exp*remain
                # cur_max = i   # 当使用c++ java时需要考虑数据溢出的问题，每次求乘积时都需要求余数
                # for _ in exp:
                #     cur_max *= cur_max % 1000000007
            if cur_max > max_multi:
                max_multi = cur_max
            else:
                break

        return max_multi % 1000000007


if __name__ == "__main__":
    solution = Solution()
    n = 40
    print(solution.cuttingRope(n))
