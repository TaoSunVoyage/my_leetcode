#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (29.98%)
# Likes:    2135
# Dislikes: 85
# Total Accepted:    233.5K
# Total Submissions: 738.5K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#
class Solution:
    # DP - top-down
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        return self.helper(coins, amount, {})
    
    def helper(self, coins, remain, count):
        if remain < 0: 
            return -1
        if remain == 0:
            return 0
        if count.get(remain, 0) != 0:
            return count[remain]
        minValue = float("inf")
        for coin in coins:
            res = 1 + self.helper(coins, remain - coin, count)
            if res > 0 and res < minValue:
                minValue = res
        count[remain] = -1 if minValue == float("inf") else minValue
        return count[remain]
    
    # DP - botton-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[amount] > amount else dp[amount]



