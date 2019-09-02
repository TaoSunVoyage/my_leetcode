#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
# https://leetcode.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (63.14%)
# Likes:    670
# Dislikes: 59
# Total Accepted:    43.2K
# Total Submissions: 67.4K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.
# 
# Example 1:
# 
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 
# 
# Note:
# 
# 
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# 
# 
#
class Solution:
    # My solution
    def shortestToChar(self, S: str, C: str) -> List[int]:
        charInd = [i for i in range(len(S)) if S[i] == C]
        res = [min(abs(i - cInd) for cInd in charInd) for i in range(len(S))]
        return res


