#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.85%)
# Likes:    458
# Dislikes: 127
# Total Accepted:    234.3K
# Total Submissions: 556.8K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 2^0 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 2^4 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution:
    # My solution
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        while n:
            if n & 1 == 1 and n != 1:
                return False
            n >>= 1
        return True
    # My solution
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        return  not (n % 2) and self.isPowerOfTwo(n // 2)
    
    # Most-voted
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and n & (n - 1) == 0


