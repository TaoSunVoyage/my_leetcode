#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    # my solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        start = 0
        for end in range(len(s)):
            while s[end] in s[start:end]:
                start += 1
            maxlen = max(maxlen, end - start + 1)
        return maxlen
    
    # 
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = start = 0
        # use a dict to store the char position
        usedChar = {}
        for end in range(len(s)):
            if s[end] in usedChar and start <= usedChar[s[end]]:
                start = usedChar[s[end]] + 1
            else:
                maxlen = max(maxlen, end - start + 1)
            usedChar[s[end]] = end
        return maxlen
