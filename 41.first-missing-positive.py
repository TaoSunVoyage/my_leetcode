#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.69%)
# Likes:    1615
# Dislikes: 560
# Total Accepted:    210.2K
# Total Submissions: 729.7K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#
class Solution:
    # O(n^2)
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        while True:
            for i in range(len(nums)):
                if nums[i] == missing:
                    missing += 1
                    break
            else:
                break
        return missing

    # O(nlogn)
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1
        for i in range(len(nums)):
            if nums[i] == missing:
                missing += 1
        return missing

    # O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    # O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        # delete those useless elements
        for i in range(len(nums)): 
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # use the index as the hash to record the frequency of each number
        for i in range(len(nums)): 
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n

