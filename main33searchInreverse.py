class Solution:
    def search(self, nums, target: int) -> int:
        return self.recBinarySearch(nums, 0, len(nums)-1, target)
    
    def recBinarySearch(self, nums, left, right, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        if right - left == 1:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

        mid = (left+right)//2
        if nums[mid] > nums[left]:
            if target < nums[mid] and target >= nums[left]:
                return self.recBinarySearch(nums, left, mid-1, target)
            else:
                return self.recBinarySearch(nums, mid, right, target)
        else:
            if target > nums[mid] and target <= nums[right]:
                return self.recBinarySearch(nums, mid+1, right, target)
            else:
                return self.recBinarySearch(nums, left, mid, target)


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5]
    print(solution.search(nums, 3))
