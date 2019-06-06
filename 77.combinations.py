#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (47.15%)
# Likes:    773
# Dislikes: 45
# Total Accepted:    203.7K
# Total Submissions: 426.5K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution:
    # My solution
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return [[]]
        if not n: return []
        
        return self.combine(n - 1, k) + [ c + [n]  for c in self.combine(n - 1, k - 1)]
    
    # Most-voted solution
    # recursive
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in self.combine(i - 1, k - 1)]
    # iterative
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        return combs
