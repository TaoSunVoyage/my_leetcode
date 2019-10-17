#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.36%)
# Likes:    431
# Dislikes: 35
# Total Accepted:    22K
# Total Submissions: 47.5K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        fresh, rotten = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while True:
            if fresh and not rotten:
                return -1
            if not fresh:
                return minutes
            nextRotten = []
            for i, j in rotten:
                target = [(i - 1, j), (i, j - 1),
                          (i + 1, j), (i, j + 1)]
                for i, j in target:
                    if (i, j) in fresh:
                        fresh.remove((i, j))
                        nextRotten.append((i, j))
            minutes += 1
            rotten = nextRotten

# @lc code=end

