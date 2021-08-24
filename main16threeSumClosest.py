class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        res = 999999
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                cur = target - nums[i] - nums[j] - nums[k]
                if abs(cur) < abs(target - res):
                    res = nums[i] + nums[j] + nums[k]
                if cur > 0:
                    j += 1
                elif cur < 0:
                    k -= 1
                else:
                    return target
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [0,2,1,-3]
    target = 1
    print(solution.threeSumClosest(nums, target))