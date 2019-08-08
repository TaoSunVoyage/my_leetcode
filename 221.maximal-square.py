#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (32.77%)
# Likes:    1357
# Dislikes: 34
# Total Accepted:    135.4K
# Total Submissions: 405.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#
class Solution:
    # My Solution
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    minNeighbor = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                    matrix[i][j] = minNeighbor + 1
                res = max(res, matrix[i][j])

        return res ** 2

