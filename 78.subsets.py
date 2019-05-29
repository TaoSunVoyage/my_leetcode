#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (52.29%)
# Likes:    1888
# Dislikes: 50
# Total Accepted:    365.5K
# Total Submissions: 692.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    # My solution
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [nums]
        return self.subsets(nums[1:]) + [s + [nums[0]] for s in self.subsets(nums[1:])]

    # My solution - bit manipulation
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2 ** len(nums)):
            subset = []
            for j in range(len(nums)):
                if not i: 
                    break
                if i % 2:
                    subset.append(nums[j])
                i >>= 1
            res.append(subset)
        return res
            

