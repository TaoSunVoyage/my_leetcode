#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (54.66%)
# Likes:    1951
# Dislikes: 59
# Total Accepted:    375.5K
# Total Submissions: 682.6K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution:
    # My Solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        result = []
        for n in nums:
            otherNums = nums.copy()
            otherNums.remove(n)
            result += [[n] + i for i in self.permute(otherNums)]
        return result

    # Most-voted Solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)



