#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (66.03%)
# Likes:    363
# Dislikes: 46
# Total Accepted:    32.8K
# Total Submissions: 50K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
# 
# 
# 
#

# @lc code=start
from collections import Counter
from functools import reduce
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        c = reduce(lambda x, y: Counter(x) & Counter(y), A)
        return [i for i in c for _ in range(c[i])]
# @lc code=end

