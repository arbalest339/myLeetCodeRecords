class Solution:
    def maxProfit1(self, prices) -> int:
        """
        只能投资一次，求最大收益
        记录当前天之前的价格最低买入天
        """
        if len(prices)<2:
            return 0
        buy = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[buy]:
                profit = max(prices[i] - prices[buy], profit)
            if prices[i] < prices[buy]:
                buy = i
        return profit
    
    def maxProfit2(self, prices) -> int:
        """
        能投资无数次，但同时刻只能投资一笔，求最大收益
        只要知道第二天要跌，前一天就卖
        """
        if len(prices) <= 1:
            return 0
        
        buy = 0
        last = 0
        cur = 1
        profit = 0
        while cur < len(prices):
            if prices[last]>prices[cur]:
                profit += prices[last]-prices[buy]
                buy = cur
            last = cur
            cur += 1
        
        profit += prices[last]-prices[buy]
        return profit

    def maxProfit3(self, prices) -> int:
        profits = [[0]*len(prices) for _ in range(len(prices))]

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profits[j][i] = prices[j] - prices[i]
        
        cur_max = 0
        day_max = [max(profits[i]) for i in range(len(prices))]
        for i, p in enumerate(day_max):
            next_max = 0
            for ni in range(i+1, len(prices)):
                for j in range(i+1, ni):
                    next_max = max(next_max, profits[ni][j])
            cur_max = max(cur_max, p+next_max)
        
        return cur_max
    
    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);  

        return max(sell[n - 1])


if __name__ == "__main__":
    solution = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(solution.maxProfit1(prices))
    print(solution.maxProfit2(prices))
    print(solution.maxProfit3(prices))