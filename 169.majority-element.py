#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (52.28%)
# Likes:    1674
# Dislikes: 147
# Total Accepted:    389K
# Total Submissions: 736.5K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    # My solution
    import collections
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common(1)[0][0]
    # My solution
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        threshold = len(nums) // 2
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] > threshold:
                return n
    # Most voted
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
    
