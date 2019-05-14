#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.34%)
# Likes:    1709
# Dislikes: 522
# Total Accepted:    233.3K
# Total Submissions: 767.5K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    # naive solution
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        if len(nums) == 2: 
            nums[0], nums[1] = nums[1], nums[0]
            return
        
        # 1,2,3 -> 1,3,2
        tail = nums[1:].copy()
        self.nextPermutation(tail)
        flag = False
        for i in range(len(tail)):
            if tail[i] > nums[i+1]:
                flag = True
                break
            elif tail[i] == nums[i+1]:
                continue
            else:
                break
        if flag:
            nums[1:] = tail
            return
        
        nums[1:] = sorted(nums[1:])
        # 3,2,1 -> 1,2,3
        if nums[-1] <= nums[0]:
            nums[:-1], nums[-1] = nums[1:], nums[0]
            return
        
        # 1,3,2 -> 2,1,3
        for i in range(1, len(nums)):
            if nums[i] > nums[0]:
                nums[0], nums[i] = nums[i], nums[0]
                return

    # two loops
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums: return None

        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                j = i - 1
                break
        else:
            nums.reverse()
            return

        for i in range(len(nums) - 1, j, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1:] = nums[-1:j:-1]
                return

       
