class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

# 背包问题求排列组合数，要逐步加码物品
# 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
# 如果求排列数就是外层for遍历背包，内层for循环遍历物品。