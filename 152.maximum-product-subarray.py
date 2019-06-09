#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.01%)
# Likes:    2080
# Dislikes: 92
# Total Accepted:    212.6K
# Total Submissions: 725.2K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    # TLE
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                res = max(res, product)
        return res
    
    # Prefix product / Suffix product
    def maxProduct(self, nums: List[int]) -> int:
        # upper-case -> positive
        # lower-case -> negative
        # aBcD  -> max is 'aBcD'
        # aBcDe -> max is max('aBcD', 'BcDe')
        numsR = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            numsR[i] *= numsR[i - 1] or 1
        return max(nums + numsR)
    
    # Keep track of two things: 
    # biggest and smallest product so far
    def maxProduct(self, nums: List[int]) -> int:
        # nums:  1, 0, 4, -2,  3, -4
        # big:   1, 0, 4,  0,  3, 96
        # small: 1, 0, 0, -8,-24,-12
        # res:   1, 1, 4,  4,  4, 96
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum

