#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (46.15%)
# Likes:    1624
# Dislikes: 108
# Total Accepted:    336.7K
# Total Submissions: 720.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution:
    # My solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapper = {}
        i = 0
        for str in strs:
            key = ''.join(sorted(str))
            if key not in mapper:
                mapper[key] = i
                res.append([str])
                i += 1
            else:
                res[mapper[key]].append(str)
        return res
    
    # Most-voted solution
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
    

