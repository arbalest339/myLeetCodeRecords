class Solution:
    def maxSubArray(self, nums) -> int:
        bestVal = [nums[0]]
        for i in range(1, len(nums)):
            if bestVal[-1] > 0:
                bestVal.append(bestVal[-1]+nums[i])
            else:
                bestVal.append(nums[i])
        
        return max(bestVal)

if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution.maxSubArray(nums)