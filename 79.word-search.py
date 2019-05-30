#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (31.01%)
# Likes:    1740
# Dislikes: 84
# Total Accepted:    282.1K
# Total Submissions: 902.6K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution:
    # My solution
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        m, n = len(board), len(board[0])
        if m * n < len(word): return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if self.dfs(board, i, j, word[1:]):
                        return True
                    board[i][j] = word[0]
        return False
        
    def dfs(self, board, startX, startY, word):
        if not word: return True
        grid = [(startX, startY - 1), (startX, startY + 1), 
                (startX - 1, startY), (startX + 1, startY)]
        for i, j in grid:
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
                board[i][j] = "#"  # avoid visit again
                if self.dfs(board, i, j, word[1:]):
                    return True
                board[i][j] = word[0]
        return False
        
    
    # Most-voted Solution
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit again 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

