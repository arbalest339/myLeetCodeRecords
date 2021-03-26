class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        cur_min = 9999999
        for n in prices:
            cur_profit = n - cur_min
            max_profit = max(cur_profit, max_profit)
            cur_min = min(cur_min, n)
        return max_profit


if __name__ == "__main__":
    solution = Solution()
    nums = [7,6,4,3,1]
    solution.maxProfit(nums)