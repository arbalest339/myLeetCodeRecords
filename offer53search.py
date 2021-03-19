class Solution:
    def search(self, nums, target: int) -> int:
        if target in nums:
            start = nums.index(target)
        else:
            return 0

        res = 0
        i = start
        while i < len(nums) and nums[i] == target:
            res += 1
            i += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution.search(nums, target)
