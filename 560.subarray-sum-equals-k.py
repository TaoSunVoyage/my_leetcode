#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (42.11%)
# Likes:    1918
# Dislikes: 50
# Total Accepted:    102K
# Total Submissions: 242K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#
class Solution:
    # # TLE
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     count = 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums) + 1):
    #             if sum(nums[i:j]) == k:
    #                 count += 1
    #     return count

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     ijSum = {}
    #     count = 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums) + 1):
    #             if (i, j - 1) in ijSum:
    #                 sumIJ = ijSum[(i, j - 1)] + nums[j - 1]
    #             elif (i + 1, j) in ijSum:
    #                 sumIJ = ijSum[(i - 1, j)] - nums[i - 1]
    #             else:
    #                 sumIJ = sum(nums[i:j])
    #             ijSum[(i, j)] = sumIJ
    #             if sumIJ == k:
    #                 count += 1
    #     return count

    # Most-voted solution
    # SUM(i to j) = ACCSUM(0 to j) - ACCSUM(0 to i - 1)
    # --> TWO-SUM PROBLEM <--
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        accumulatedSum = 0
        mapper = {0: 1}
        for num in nums:
            accumulatedSum += num
            if accumulatedSum - k in mapper:
                count += mapper[accumulatedSum - k]
            if accumulatedSum not in mapper:
                mapper[accumulatedSum] = 1
            else:
                mapper[accumulatedSum] += 1
        return count
            
