#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (43.09%)
# Likes:    474
# Dislikes: 165
# Total Accepted:    204.2K
# Total Submissions: 468K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    # My solution - recursion
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        previousRow = self.getRow(rowIndex - 1)
        row = []
        for i in range(len(previousRow) - 1):
            row.append(previousRow[i] + previousRow[i + 1])
        row = [1] + row + [1]
        return row
    
    # Most-voted solution
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row

    # Mathematics
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for m in range(1, rowIndex // 2 + 1):
            row[m] = row[rowIndex - m] = int((row[m - 1] * (rowIndex - m + 1)) / m)
        return row

