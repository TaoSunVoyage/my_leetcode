#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.66%)
# Likes:    467
# Dislikes: 107
# Total Accepted:    114.6K
# Total Submissions: 286.5K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution:
    # My solution
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            diff = mid ** 2 - num
            if diff == 0:
                return True
            elif diff > 0:
                r = mid - 1
            else:
                l = mid + 1
        return False
    
    # Most-voted
    # 1 + 3 + 5 + 7 + ... + (2n - 1) = n ^ 2
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        x, i = 0, 1
        while x < num:
            x += i
            i += 2
        return x == num
            

