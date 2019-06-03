#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (41.42%)
# Likes:    1829
# Dislikes: 86
# Total Accepted:    207.7K
# Total Submissions: 498.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    # O(nlogn + n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums.sort()
        length = 1
        maxLength = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] - nums[i - 1] == 1:
                    length += 1
                    maxLength = max(maxLength, length)
                else: 
                    length = 1
        return maxLength
    
    # O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set: # O(1) look up
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set: # O(1) look up -> max n times
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

