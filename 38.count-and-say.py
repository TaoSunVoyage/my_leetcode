#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (40.21%)
# Likes:    733
# Dislikes: 5683
# Total Accepted:    278.9K
# Total Submissions: 691.4K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    # My Solution
    def countAndSay(self, n: int) -> str:
        result = ['1']
        for i in range(n - 1):
            count = 0
            newResult = []
            preNumber = None
            while result:
                number = result.pop(0)
                if number == preNumber:
                    count += 1
                else:
                    if count:
                        newResult += [str(count), preNumber]
                    count = 1
                    preNumber = number
            if count:
                newResult += [str(count), preNumber]
            result = newResult
        return ''.join(result)
    
    # Most-voted Solution
    import re
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            # the whole regular expression is group 0
            # (...) by order is group 1, 2, 3, etc.
            # \number matches the contents of the group of the same number
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
