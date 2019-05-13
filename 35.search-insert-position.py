#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        index = len(nums)//2
        pivot = nums[index]
        if target > pivot:
            return index + 1 + self.searchInsert(nums[index+1:], target)
        elif target < pivot:
            return self.searchInsert(nums[:index], target)
        else:
            return index

