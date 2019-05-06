#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        q, r = len(s) // (numRows * 2 - 2), len(s) % (numRows * 2 - 2)
        numCols = q * (numRows - 1) + 1 * (r > 0) + (r - numRows) * (r - numRows > 0) 

        z = [['' for _ in range(numCols)] for _ in range(numRows)]
        x, y = 0, 0
        isDiagnol = False
        
        for c in s:
            if isDiagnol:
                z[x][y] = c
                x -= 1
                y += 1
                isDiagnol = not (x == 0)
            else:
                z[x][y] = c
                x += 1
                isDiagnol = x == (numRows - 1)
        
        return ''.join([''.join(zz) for zz in z])


