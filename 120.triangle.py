#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (39.03%)
# Likes:    1156
# Dislikes: 124
# Total Accepted:    185.4K
# Total Submissions: 467.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution:
    # TLE
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        triangleLeft = [l[:-1] for l in triangle[1:]]
        triangleRight = [l[1:] for l in triangle[1:]]
        return triangle[0][0] + min(self.minimumTotal(triangleLeft), self.minimumTotal(triangleRight))
    # My solution - bottom to top
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        candidates = [0] * n
        for i in range(n - 1, 0, -1):
            candidates = [
                min(triangle[i][k]     + candidates[k], 
                    triangle[i][k + 1] + candidates[k + 1]) 
                for k in range(i)
            ]
        return candidates[0] + triangle[0][0]
