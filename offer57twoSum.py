class Solution:
    def twoSum(self, nums, target: int):
        i = 0
        j = len(nums) - 1
        while nums[j] > target:
            j -= 1
        while i < j:
            if  nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

if __name__ == "__main__":
    solution = Solution()
    nums = [10,26,30,31,47,60]
    target = 40
    solution.twoSum(nums, target)