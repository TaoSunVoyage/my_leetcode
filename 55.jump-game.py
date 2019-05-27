#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (31.73%)
# Likes:    1894
# Dislikes: 193
# Total Accepted:    262.9K
# Total Submissions: 824.6K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#
class Solution:
    # My Solution
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        # from start to end -> where it can jump to
        start, end = 0, 0
        maxend = 0
        while start <= end:
            for i in range(start, end + 1):
                maxend = max(maxend, i + nums[i])
                if maxend >= len(nums) - 1:
                    return True
            start = end + 1
            end = maxend
        return False
    
    # Most-voted solution
    # linear
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
    # backtracking
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

        

