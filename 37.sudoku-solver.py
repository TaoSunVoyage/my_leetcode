#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (36.43%)
# Likes:    830
# Dislikes: 56
# Total Accepted:    126.7K
# Total Submissions: 345.8K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#
class Solution:
    # straightforward backtracking
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        return
    
    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    for c in '123456789':
                        if self.isValid(i, j, c):
                            self.board[i][j] = c
                            if self.solve():
                                return True
                            else:
                                self.board[i][j] = '.'
                    return False
        return True

    def isValid(self, row, col, val):
        for i in range(9):
            # row
            if self.board[row][i] == val: return False
            # col
            if self.board[i][col] == val: return False
            # box
            if self.board[row//3*3+ i//3][col//3*3 + i%3] == val: return False
        return True
    
    