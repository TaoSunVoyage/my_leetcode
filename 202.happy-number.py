#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (44.91%)
# Likes:    905
# Dislikes: 235
# Total Accepted:    243.3K
# Total Submissions: 532.4K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#
class Solution:
    # My solution
    def isHappy(self, n: int) -> bool:
        def sumOfDigitSquare(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            return res
        cache = []
        while True:
            if n == 1:
                return True
            if n in cache:
                return False
            cache.append(n)
            n = sumOfDigitSquare(n)


