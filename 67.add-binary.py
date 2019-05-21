#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.78%)
# Likes:    941
# Dislikes: 187
# Total Accepted:    300.5K
# Total Submissions: 770.2K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    # My Solution
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]

    # My Solution with full-adder
    def add(self, a: int, b: int, c_in: int) -> (int, int):
        s = a ^ b ^ c_in
        c_out = a & b | (c_in & (a ^ b))
        return s, c_out

    def addBinary(self, a: str, b: str) -> str:
        c = 0
        i = 1
        result = []
        for i in range(1, max(len(a), len(b)) + 1):
            if i > len(a):
                s, c = self.add(0, int(b[-i]), c)
            elif i > len(b):
                s, c = self.add(int(a[-i]), 0, c)
            else:
                s, c = self.add(int(a[-i]), int(b[-i]), c)
            result.insert(0, str(s))
        if c:
            result.insert(0, str(c))
        return ''.join(result)
    
    # Most-voted solution
    def addBinary(self, a: str, b: str) -> str:
        if not a: return b
        if not b: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        return self.addBinary(a[:-1], b[:-1]) + '1'
