#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (41.17%)
# Likes:    2683
# Dislikes: 99
# Total Accepted:    368.8K
# Total Submissions: 881.5K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    self.sink(i, j)
                    res += 1
        return res
    
    def sink(self, i, j):
        if self.grid[i][j] == '1':
            self.grid[i][j] = '0'
            if j - 1 >= 0:
                self.sink(i, j - 1)
            if j + 1 < len(self.grid[0]):
                self.sink(i, j + 1)
            if i - 1 >= 0:
                self.sink(i - 1, j)
            if i + 1 < len(self.grid):
                self.sink(i + 1, j)


