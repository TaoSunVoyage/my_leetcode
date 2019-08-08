#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (49.23%)
# Likes:    2580
# Dislikes: 293
# Total Accepted:    198.6K
# Total Submissions: 396.5K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#
class Solution:
    # TLE - O(1) space O(N^2) time
    def findDuplicate(self, nums: List[int]) -> int:
        for n in range(1, len(nums)):
            count = 0
            for i in range(len(nums)):
                if nums[i] == n:
                    count += 1
                    if count > 1:
                        return n
    
    # My solution - O(N) space O(N) time
    import collections
    def findDuplicate(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

    # O(1) space O(N) time
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
        

