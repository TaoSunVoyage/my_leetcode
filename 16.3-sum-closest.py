#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    # Slow ...
    # def twoSumClosest(self, nums: List[int], target: int) -> int:
    #     nums = sorted(nums)
    #     i = 0
    #     j = len(nums) - 1
    #     min_gap = None
    #     while i < j:  
    #         sum2 = nums[i] + nums[j]
    #         gap = sum2 - target
    #         if min_gap is None:
    #             min_gap = abs(gap)
    #             closest = sum2
    #         if abs(gap) < min_gap:
    #             min_gap = abs(gap)
    #             closest = sum2
    #         if gap == 0:
    #             break
    #         elif gap > 0:
    #             j -= 1
    #         else:
    #             i += 1
    #     return closest

            
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums = sorted(nums)
    #     min_gap = None
    #     for i in range(len(nums)):
    #         temp = nums.copy()
    #         temp.pop(i)
    #         sum3 = nums[i] + self.twoSumClosest(temp, target - nums[i])
    #         gap = sum3 - target
    #         if min_gap is None:
    #             min_gap = abs(gap)
    #             closest = sum3
    #         if abs(gap) < min_gap:
    #             min_gap = abs(gap)
    #             closest = sum3
    #         if gap == 0:
    #             break
    #     return closest

    # Clean version
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = sum(nums[:3])
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == target:
                    return target
                elif sum3 < target:
                    l += 1
                else:
                    r -= 1
                if abs(sum3 - target) < abs(result - target):
                    result = sum3
        return result
                


