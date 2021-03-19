class Solution:
    def minNumber(self, nums) -> str:
        from functools import cmp_to_key

        def compare(x, y):
            if len(x) == len(y):
                for xc, yc in zip(x, y):
                    if xc > yc:
                        return 1
                    elif xc < yc:
                        return -1
                return 0
            else:
                if x+y > y+x:
                    return 1
                elif y+x > x+y:
                    return -1
                return 0
        nums = [str(n) for n in nums]
        nums = sorted(nums, key=cmp_to_key(compare))
        return "".join(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 30, 34, 5, 9]
    solution.minNumber(nums)
