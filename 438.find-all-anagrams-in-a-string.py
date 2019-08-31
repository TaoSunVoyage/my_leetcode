#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (37.04%)
# Likes:    1730
# Dislikes: 136
# Total Accepted:    135.4K
# Total Submissions: 358.6K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
# My solution
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        counterP = Counter(p)
        counterS = Counter(s[:len(p)])
        if counterP == counterS:
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            counterS[s[i - 1]] -= 1
            if not counterS[s[i - 1]]:
                del counterS[s[i - 1]]
            counterS[s[i + len(p) - 1]] += 1
            if counterP == counterS:
                res.append(i)
        return res
            

