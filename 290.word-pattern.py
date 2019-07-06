#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (34.82%)
# Likes:    653
# Dislikes: 81
# Total Accepted:    144.3K
# Total Submissions: 410.4K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#
class Solution:
    # My Solution
    def wordPattern(self, pattern: str, str: str) -> bool:
        pList = list(pattern)
        sList = str.split()
        if len(pList) != len(sList):
            return False
        n = len(pList)
        sTop = {}
        pTos = {}
        for i in range(n):
            if sList[i] not in sTop and pList[i] not in pTos:
                sTop[sList[i]] = pList[i]
                pTos[pList[i]] = sList[i]
            else:
                if sTop.get(sList[i], '') != pList[i] or pTos.get(pList[i], '') != sList[i]:
                    return False
        return True
    
    # Most-voted
    def wordPattern(self, pattern: str, str: str) -> bool:
        pList = list(pattern)
        sList = str.split()
        return list(map(pList.index, pList)) == list(map(sList.index, sList))
    
    def wordPattern(self, pattern: str, str: str) -> bool:
        pList = list(pattern)
        sList = str.split()
        return len(set(zip(pList, sList))) == len(set(pList)) == len(set(sList)) and len(pList) == len(sList)
