class Solution:
    def single2Numbers(self, nums):
        import functools
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:   # 寻找某一位不为0的地方，由于存在不相同的两个数，二进制异或一定有不为零的部分
            div <<= 1
        a, b = 0, 0
        for n in nums:   # 按照第 i 位给原来的序列分组
            if n & div:
                a ^= n  # 分组内部进行异或，相同的数相应位也相同，必然在同一组
            else:
                b ^= n
        return [a, b]

    def singleNumber(self, nums):
        bytePlaces = [0]*32
        for n in nums:
            places = bin(n)[2:]
            for i in range(1, len(places)+1):
                bytePlaces[-i] += int(places[-i])

        res = 0
        for b in bytePlaces:
            res *= 2
            res += b%3
            
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [4,10,4,10,2,4,10]
    solution.singleNumber(nums)
