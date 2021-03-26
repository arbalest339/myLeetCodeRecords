class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums or k<=0:
            return []
        max_num = max(nums[:k])
        res = [max_num]
        for i in range(k, len(nums)):
            if max_num == nums[i-k]:
                max_num = max(nums[i-k+1:i+1])
                res.append(max_num)
            else:
                max_num = max(max_num, nums[i])
                res.append(max_num)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution.maxSlidingWindow(nums, k)