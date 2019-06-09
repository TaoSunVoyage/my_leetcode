#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.69%)
# Likes:    468
# Dislikes: 1288
# Total Accepted:    120.4K
# Total Submissions: 762.5K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    # Numerical unstable 94911151 / 94911152 == 94911150 / 94911151
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points: return 0
        mapper = {}
        res = 1

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        def frac(x,y):
            g = gcd(x,y)
            return x//g, y//g

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                # Y = a * X + b
                # if x2 == x1 -> X = a, b = None
                a = frac((y2 - y1), (x2 - x1)) if x2 - x1 else x1
                b = frac((y1 * x2 - y2 * x1), (x2 - x1)) if x2 - x1 else None
                if (a, b) in mapper:
                    mapper[(a, b)].add(i)
                    mapper[(a, b)].add(j)
                else:
                    mapper[(a, b)] = set([i, j])
                res = max(res, len(mapper[(a, b)]))
        return res
        

