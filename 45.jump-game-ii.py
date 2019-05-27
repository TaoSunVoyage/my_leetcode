#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.89%)
# Likes:    1140
# Dislikes: 57
# Total Accepted:    168.6K
# Total Submissions: 601.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution:
    # TLE
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def helper(nums, startIdx):
            lastIdx = len(nums) - 1
            if startIdx in cache:
                return cache[startIdx]
            nJumps = len(nums)
            for step in range(1, nums[startIdx] + 1):
                jumpTo = startIdx + step
                if jumpTo > lastIdx:
                    break
                elif jumpTo == lastIdx:
                    nJumps = 1
                    break
                else:
                    nextJumps = helper(nums, jumpTo)
                    if nextJumps:
                        nJumps = min(nJumps, 1 + nextJumps)
            if nJumps == len(nums):
                cache[lastIdx] = 0
            else:
                cache[lastIdx] = nJumps
            return cache[lastIdx]
        return helper(nums, 0)

    # TLE
    def jump(self, nums: List[int]) -> int:
        jumps = [0]
        length = len(nums)
        if length == 1:
            return 0
        # back-tracking
        for i in range(length - 2, -1, -1):
            if nums[i] >= length - i - 1:
                minJumps = 0
            else:
                minJumps = length
                for n in jumps[:nums[i]]:
                    if n!= -1:
                        minJumps = min(minJumps, n)
            if minJumps == length:
                jumps.insert(0, -1)
            else:
                jumps.insert(0, 1 + minJumps)
        return jumps[0]

    # Most-voted solution
    # BFS problem!
    def jump(self, nums: List[int]) -> int:
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1 # how far it can jumps to in this jump
            # loop through index covered in this jump
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

