#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    # Time Limit Eceeeded
    # def twoSum(self, nums: List[int], sum_: int) -> List[List[int]]:
    #     map = {}
    #     result = []
    #     for i in range(len(nums)):
    #         if sum_ - nums[i] not in map:
    #             map[sum_ - nums[i]] = i
    #     for i in range(len(nums)):
    #         if nums[i] in map and i != map[nums[i]]:
    #             pair = sorted([nums[i], nums[map[nums[i]]]])
    #             if pair not in result:
    #                 result.append(pair)
    #     return result
    
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     for i in range(len(nums)):
    #         temp = nums.copy()
    #         _ = temp.pop(i)
    #         i_pair = self.twoSum(temp, - nums[i])
    #         for p in i_pair:
    #             pair = sorted([nums[i]] + p)
    #             if pair not in result:
    #                 result.append(pair)
    #     return result

    # Time Limit Exceeded
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     nums = sorted(nums)
    #     for i in range(len(nums)):
    #         j = i + 1
    #         k = len(nums) - 1
    #         while (j < k):
    #             if nums[j] + nums[k] == -nums[i]:
    #                 pair = [nums[i], nums[j], nums[k]]
    #                 if pair not in result:
    #                     result.append(pair)
    #                 j += 1
    #                 k -= 1
    #             elif nums[j] + nums[k] < -nums[i]:
    #                 j += 1
    #             else:
    #                 k -= 1
    #     return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                elif s > 0:
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result
