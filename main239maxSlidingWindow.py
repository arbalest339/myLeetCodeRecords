class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans


if __name__=="__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    solution.maxSlidingWindow(nums, k)