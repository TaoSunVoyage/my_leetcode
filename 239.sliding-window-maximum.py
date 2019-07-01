#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (37.83%)
# Likes:    1656
# Dislikes: 95
# Total Accepted:    158.2K
# Total Submissions: 414.7K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#
class Solution:
    # My solution - O(nk)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i+k]))
        return res
    
    # My solution - O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        l = []
        res = []
        for i in range(k):
            while l and nums[l[-1]] <= nums[i]:
                _ = l.pop()
            l.append(i)
        
        for i in range(k, len(nums)):
            res.append(nums[l[0]])
            if l[0] == i - k:
                _ = l.pop(0)
            while l and nums[l[-1]] <= nums[i]:
                _ = l.pop()
            l.append(i)
        res.append(nums[l[0]])
        return res
    
    
    # Nice version
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not k:
            return []
        l = []
        res = []
        for i, n in enumerate(nums):
            while l and nums[l[-1]] <= n:
                _ = l.pop()
            if l and l[0] == i - k:
                _ = l.pop(0)
            l.append(i)
            if i >= k - 1:
                res.append(nums[l[0]])
        return res


    


