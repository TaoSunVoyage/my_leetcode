#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (47.94%)
# Likes:    1914
# Dislikes: 57
# Total Accepted:    335.8K
# Total Submissions: 696.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution:
    # my solution
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1 and candidates[0] == target:
                return [ candidates ]
        result = []
        for i in range(len(candidates)):
            remain = target - candidates[i]
            if remain > 0:
                remainCombination = self.combinationSum(candidates[i:], remain)
                result += [ [candidates[i]] + c for c in remainCombination ]
            elif remain == 0:
                result += [ [candidates[i]] ]
            else:
                continue
        return result

    # most-voted solution
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, candidates, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], result)


