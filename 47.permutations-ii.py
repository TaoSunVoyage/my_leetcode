#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (40.09%)
# Likes:    992
# Dislikes: 44
# Total Accepted:    244.5K
# Total Submissions: 602.6K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:
    # My solution
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res
        

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        self.dfs(nums[1:], path + [nums[0]], res)
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
    
    # Most-voted solution
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ret = [[]]
        for n in nums:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    # if i is not the last one and seq[i] is duplicated
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret



