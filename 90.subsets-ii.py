#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (42.10%)
# Likes:    874
# Dislikes: 50
# Total Accepted:    204.1K
# Total Submissions: 480.4K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution:
    # My solution
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                break
            i = i + 1
        return [[nums[0]] * k + s for s in self.subsetsWithDup(nums[i: ]) for k in range(i + 1)]
    
    # Most-voted
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

