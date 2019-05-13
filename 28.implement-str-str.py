#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(needle) > len(haystack): return -1
        l, r = 0, len(needle) - 1
        while r < len(haystack):
            if haystack[l:r+1] == needle:
                return l
            l += 1
            r += 1
        return -1
        

