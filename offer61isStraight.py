class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        zero = 0
        last = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zero += 1
                i += 1
            elif last == 0:
                last = nums[i]
                i += 1
            elif nums[i] != last+1:
                if zero > 0:
                    zero -= 1
                    last += 1
                else:
                    return False
            else:
                last = nums[i]
                i += 1
        return True

if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,2,3,5]
    solution.isStraight(nums)