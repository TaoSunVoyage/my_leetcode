#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (47.28%)
# Likes:    1994
# Dislikes: 167
# Total Accepted:    373.4K
# Total Submissions: 781.4K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution:
    # My solution - sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    
    # My solution - quick select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[k - 1]
        smaller, same, larger = [], [], []
        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            elif nums[i] > pivot:
                larger.append(nums[i])
            else:
                same.append(nums[i])
        if len(larger) >= k:
            return self.findKthLargest(larger, k)
        elif len(larger) + len(same) >= k:
            return pivot
        else:
            return self.findKthLargest(smaller, k - len(larger + same))

    # Heap
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
    




