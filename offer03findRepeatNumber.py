class Solution:
    def findRepeatNumber(self, nums) -> int:
        for idx in range(len(nums)):
            while nums[idx] != idx:     # 发现这个坑的萝卜不是自己家的
                if nums[idx] == nums[nums[idx]]:  # 如果发现这个萝卜它家里有了和它一样的萝卜
                    return nums[idx]            # 说明这个萝卜是双胞胎，将它上交国家

                # 把这个萝卜送回它家去，然后把它家里的萝卜拿回来
                nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]


if __name__ == "__main__":
    input = [2, 3, 1, 0, 2, 5, 3]
    solution = Solution()
    print(solution.findRepeatNumber(input))
