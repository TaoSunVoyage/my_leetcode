#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
class Solution:
    # O(m+n) time complexity
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     nums = nums1 + nums2
    #     nums = sorted(nums)
    #     if len(nums) % 2:
    #         return nums[len(nums) // 2]
    #     else:
    #         return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        
    # Another approach
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     m = len(nums1)
    #     n = len(nums2)
    #     looked = []
    #     while True:
    #         if not (nums1 and nums2):
    #             break
    #         if nums1[0] < nums2[0]:
    #             looked.append(nums1.pop(0))
    #         else:
    #             looked.append(nums2.pop(0))
    #         if len(looked) == (m + n) // 2 + 1:
    #             if (m + n) % 2:
    #                 return looked[-1] * 1.0
    #             else:
    #                 return (looked[-1] + looked[-2]) / 2.0
    #     all_nums = looked + nums1 + nums2
    #     if (m + n) % 2:
    #         return all_nums[(m + n) // 2] * 1.0
    #     else:
    #         return (all_nums[(m + n) // 2] + all_nums[(m + n) // 2 - 1]) / 2.0

    # O(log(m+n)) time complexity
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2

    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        i1, i2 = len(nums1) // 2, len(nums2) // 2
        m1, m2 = nums1[i1], nums2[i2]
        if i1 + i2 < k:
            if m1 < m2:
                return self.kth(nums1[i1+1:], nums2, k - i1 - 1)
            else:
                return self.kth(nums1, nums2[i2+1:], k - i2 - 1)
        else:
            if m1 < m2:
                return self.kth(nums1, nums2[:i2], k)
            else:
                return self.kth(nums1[:i1], nums2, k)
 