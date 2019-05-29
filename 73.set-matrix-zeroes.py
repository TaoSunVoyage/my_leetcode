#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (39.54%)
# Likes:    1042
# Dislikes: 190
# Total Accepted:    208.6K
# Total Submissions: 524.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution:
    # My solution O(m + n) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroRows, zeroColumns = set(), set()
        # get which row/column zero is
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroColumns.add(j)
        # set those rows/columns to 0
        for i in zeroRows:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in zeroColumns:
                matrix[i][j] = 0
    
    # Most-voted solution with O(1) space
    # Use first row/column as the indicator
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRowHasZero = not all(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    print(i, j, matrix[0][j] == 0, matrix[i][0] == 0)
                    matrix[i][j] = 0
        if firstRowHasZero:
            matrix[0] = [0] * n

