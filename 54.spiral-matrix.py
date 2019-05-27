#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (30.19%)
# Likes:    1063
# Dislikes: 405
# Total Accepted:    232.7K
# Total Submissions: 765.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution:
    # My Solution
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        # matrix shape
        rows, cols = len(matrix), len(matrix[0])
        # walls
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        # initial direction
        direction = 'right'
        # start position
        i, j = 0, -1
        res = []
        while top <= bottom and left <= right:
            if direction == 'right':
                j = j + 1
                if j == right:
                    direction = 'down'
                    top = top + 1
            elif direction == 'down':
                i = i + 1
                if i == bottom:
                    direction = 'left'
                    right = right - 1
            elif direction == 'left':
                j = j - 1
                if j == left:
                    direction = 'up'
                    bottom = bottom - 1
            elif direction == 'up':
                i = i - 1
                if i == top:
                    direction = 'right'
                    left = left + 1
            res.append(matrix[i][j])
        return res

    # Most-voted Solution
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

