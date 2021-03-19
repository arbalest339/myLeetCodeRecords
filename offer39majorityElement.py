class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        s = 0
        e = 0
        cur_num = nums[0]
        for i, num in enumerate(nums):
            if num != cur_num:
                e = i
                length = e-s
                if length > len(nums) // 2:
                    return cur_num
                s = i
                cur_num = num
        e = len(nums)
        length = e-s
        if length > len(nums) // 2:
            return cur_num
        return nums


if __name__ == "__main__":
    solution = Solution()
    input = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solution.majorityElement(input)
