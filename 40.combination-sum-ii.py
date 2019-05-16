#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (41.16%)
# Likes:    807
# Dislikes: 43
# Total Accepted:    217.8K
# Total Submissions: 526.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution:
    # my solution at first
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1 and candidates[0] == target:
                return [ candidates ]
        result = []
        candidates.sort()
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            remain = target - candidates[i]
            if remain > 0 and i + 1 < len(candidates):
                remainCombination = self.combinationSum2(candidates[i+1:], remain)
                result += [ [candidates[i]] + c for c in remainCombination ]
            elif remain == 0:
                result += [ [candidates[i]] ]
            else:
                continue
        return result  

    # back-tracking solution modified by the solution of no.39
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:     
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, candidates, target, index, path, result):
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]: 
                continue
            if candidates[i] > target:
                return
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)
