#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (36.13%)
# Likes:    892
# Dislikes: 62
# Total Accepted:    104.3K
# Total Submissions: 286.7K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
class Solution:
    # TLE
    def nthUglyNumber(self, n: int) -> int:
        i = 0
        while n:
            i = i + 1
            if self.isUglyNumber(i):
                n = n - 1
        return i
    
    def isUglyNumber(self, n):
        if n == 1:
            return True
        for i in [2, 3, 5]:
            if not n % i:
                return self.isUglyNumber(n // i)
        return False
    
    # TLE
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [
            2 ** c[0] * 3 ** c[1] * 5 ** c[2] 
            for k in range(n)
            for c in self.combinationOf3(k)
        ]
        return sorted(uglyNumbers)[n - 1]
    
    def combinationOf3(self, n):
        if n == 0:
            return [(0, 0, 0)]
        res = []
        for c in self.combinationOf3(n - 1):
            res += [
                (c[0] + 1, c[1], c[2]),
                (c[0], c[1] + 1, c[2]),
                (c[0], c[1], c[2] + 1),
            ]
        return list(set(res))

    # Most-voted
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
