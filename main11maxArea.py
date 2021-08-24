class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height)-1
        res_max = min(height[left], height[right])*(right-left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            cur_max = min(height[left], height[right])*(right-left)
            res_max = max(cur_max, res_max)
        return res_max


if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution.maxArea(height)
