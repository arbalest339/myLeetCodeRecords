class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)<=1:
            return nums
        offset = 0
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last:
                offset += 1
            else:
                last = nums[i]
                nums[i-offset] = nums[i]
        return nums[:-offset]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 3, 7, 7, 9, 11, 15]
    print(solution.removeDuplicates(nums))
