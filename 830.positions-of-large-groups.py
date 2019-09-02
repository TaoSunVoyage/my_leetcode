#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#
# https://leetcode.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (47.66%)
# Likes:    233
# Dislikes: 63
# Total Accepted:    30.4K
# Total Submissions: 63.1K
# Testcase Example:  '"abbxxxxzzy"'
#
# In a string S of lowercase letters, these letters form consecutive groups of
# the same character.
# 
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z" and "yy".
# 
# Call a group large if it has 3 or more characters.  We would like the
# starting and ending positions of every large group.
# 
# The final answer should be in lexicographic order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending
# positions 6.
# 
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# 
# 
# Example 3:
# 
# 
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# 
# 
# 
# Note:  1 <= S.length <= 1000
# 
#
class Solution:
    # My solution
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        pre, preInd, endInd = S[0], 0, 0
        for i in range(1, len(S)):
            if S[i] == pre:
                endInd = i
            else:
                if endInd - preInd >= 2:
                    res.append([preInd, endInd])
                pre, preInd, endInd = S[i], i, i
        if endInd - preInd >= 2:
            res.append([preInd, endInd])
        return res


