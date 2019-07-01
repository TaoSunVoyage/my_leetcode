#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (40.93%)
# Likes:    2606
# Dislikes: 81
# Total Accepted:    331.6K
# Total Submissions: 806.8K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
class Solution:
    # TLE
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) <= 2: 
            return max(nums)
        return max(nums[0] + self.rob(nums[2:]), 
                   nums[1] + self.rob(nums[3:]))
    
    # My solution - O(N^2)
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[j] for j in range(i - 1))
        return max(dp[-2:])
    
    # My solution - O(N)
    def rob(self, nums: List[int]) -> int:
        maxWithN, maxWithoutN = 0, 0
        for i in range(len(nums)):
            maxWithN, maxWithoutN = nums[i] + maxWithoutN, max(maxWithoutN, maxWithN)
        return max(maxWithN, maxWithoutN)    

        
