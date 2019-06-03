#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (40.47%)
# Likes:    898
# Dislikes: 36
# Total Accepted:    164.1K
# Total Submissions: 401.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "a"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                ps = self.partition(s[i:])
                if not ps:
                    ps = [[]]
                res += [[s[:i]] + p for p in ps]
        return res
    
    def isPalindrome(self, word):
        return word == word[::-1]

