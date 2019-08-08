#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (28.84%)
# Likes:    732
# Dislikes: 145
# Total Accepted:    174.8K
# Total Submissions: 600.8K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#
class Solution:
    # my solution
    def convertToTitle(self, n: int) -> str:
        mapper = {i + 1: chr(i + ord('A')) for i in range(26)}
        ans = ''
        while n :
            n, remainder = n // 26, n % 26
            if not remainder:
                n = n - 1
                remainder = 26
            ans = mapper[remainder] + ans
            
        return ans
