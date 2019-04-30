#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                return [d[nums[i]], i]
        return [-1, -1]
