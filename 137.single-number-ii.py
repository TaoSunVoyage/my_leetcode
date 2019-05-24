#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (45.69%)
# Likes:    793
# Dislikes: 254
# Total Accepted:    165.8K
# Total Submissions: 361.4K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#
class Solution:
    # My solution
    # with extra memory
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] == 3:
                _ = d.pop(num)
        return list(d)[0]
    
    # Most-voted solution
    # without extra memory
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one, two, three = one ^ num, two | (one & num), two & num
            one, two = one & ~three, two & ~three
        return one
