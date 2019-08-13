#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (43.91%)
# Likes:    606
# Dislikes: 49
# Total Accepted:    35.4K
# Total Submissions: 79.2K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string s that consists of only uppercase English letters, you can
# perform at most k operations on that string.
# 
# In one operation, you can choose any character of the string and change it to
# any other uppercase English character.
# 
# Find the length of the longest sub-string containing all repeating letters
# you can get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 10^4.
# 
# Example 1:
# 
# 
# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
# 
# 
#

from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        counter = Counter()
        for r in range(len(s)):
            counter[s[r]] += 1
            mostCommonN = counter.most_common(1)[0][1]
            if r - l + 1 - mostCommonN > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
