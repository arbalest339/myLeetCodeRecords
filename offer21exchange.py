class Solution:
    def exchange(self, nums):
        def switch(i, j):
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp

        i, j = 0, len(nums)-1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            if i < j:
                switch(i, j)

        return nums


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 3]
    print(solution.exchange(nums))
