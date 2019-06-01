#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (49.77%)
# Likes:    983
# Dislikes: 78
# Total Accepted:    268.3K
# Total Submissions: 536.1K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
from collections import Counter 
class Solution:
    # TLE
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1
    
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
    
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        candidates = []
        for i, c in enumerate(s):
            if c not in counter:
                counter[c] = i
                candidates.append(i)
            else:
                if counter[c] != -1:
                    candidates.remove(counter[c])
                    counter[c] = -1
        if not candidates:
            return -1
        return candidates[0]

        
