#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (42.81%)
# Likes:    3488
# Dislikes: 63
# Total Accepted:    288.9K
# Total Submissions: 671K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution:
    # # Time Limit Exceeded
    # def trap(self, height: List[int]) -> int:
    #     volume = {}
    #     sumVolume = 0
    #     for i in range(len(height)):
    #         for j in range(1, height[i] + 1):
    #             if j in volume:
    #                 sumVolume += i - volume[j] - 1
    #             volume[j] = i
    #     return sumVolume
    
    # My solution
    # FIRST, from right to left
    #   IF right >= left: add collected water
    # THEN, run same algorithm with unused bars from left to right
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        lo, hi = 0, 1
        collected, sumWater = 0, 0
        unused = [height[lo]]
        while lo < hi < len(height):
            if height[lo] <= height[hi]:
                sumWater += collected
                collected = 0
                lo, hi = hi, hi + 1
                unused = [height[lo]]
            else:
                collected += height[lo] - height[hi]
                unused.append(height[hi])
                hi = hi + 1
        return sumWater + self.trap(unused[::-1])

    
    # The volume of water at position i:
    #   volume[i] = min(left_max[i], right_max[i]) - height[i]
    
    # Dynamic Programming
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left_max, right_max = [height[0]], [height[-1]]
        for i in range(1, len(height)):
            left_max =  left_max + [max(height[i], left_max[-1])]
        for i in range(len(height)-1, -1, -1):
            right_max = [max(height[i], right_max[0])] + right_max
        volume = 0
        for i in range(len(height)):
            volume += min(left_max[i], right_max[i]) - height[i]
        return volume

    # Most-voted solution
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1
        return volume


    
    
