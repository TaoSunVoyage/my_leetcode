#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (40.61%)
# Likes:    2531
# Dislikes: 58
# Total Accepted:    225.9K
# Total Submissions: 552.6K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
class Solution:
    # Most-voted 
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < n:
                    i = m + 1
                else:
                    j = m
            tails[i] = n
            size = max(i + 1, size)
        return size
    
    # dynamic programming - O(N^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        res = 1
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
