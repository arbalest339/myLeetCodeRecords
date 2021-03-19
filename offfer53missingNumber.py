class Solution:
    def missingNumber(self, nums) -> int:
        i, j = 0, len(nums) - 1  # 二分查找
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


if __name__ == "__main__":
    solution = Solution()
    nums = [0]
    solution.missingNumber(nums)
