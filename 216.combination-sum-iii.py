#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (51.18%)
# Likes:    609
# Dislikes: 30
# Total Accepted:    125.4K
# Total Submissions: 241.2K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#
class Solution:
    # My submission
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, lowerBound):
            if k == 0 or n == 0 or lowerBound > n:
                return []
            if k == 1 and n < 10:
                return [[n]]
            # res = []
            # for i in range(lowerBound, 10):
            #     res += [[i] + c for c in helper(k - 1, n - i, i + 1)]
            return [[i] + c
                    for i in range(lowerBound, 10)
                    for c in helper(k - 1, n - i, i + 1)]
        return helper(k, n, 1)
    
    # recursive
    def combinationSum3(self, k, n):
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in combs(k - 1, n - last, last)]
        return combs(k, n, 10)
    # iterative
    # calculate all the combinations
    def combinationSum3(self, k, n):
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]



