#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.21%)
# Likes:    918
# Dislikes: 31
# Total Accepted:    119.6K
# Total Submissions: 338K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#
class Solution:
    # My solution
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def helper(nums):
            maxWithN, maxWithoutN = 0, 0
            for i in range(len(nums)):
                maxWithN, maxWithoutN = nums[i] + maxWithoutN, max(maxWithoutN, maxWithN)
            return max(maxWithN, maxWithoutN)
        # rob first
        robFirst = nums[0] + helper(nums[2:-1])
        # do not rob the first
        notRobFirst = helper(nums[1:])
        return max(robFirst, notRobFirst)

