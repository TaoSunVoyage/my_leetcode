#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (49.54%)
# Likes:    842
# Dislikes: 45
# Total Accepted:    72.3K
# Total Submissions: 145.5K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
# 
# Example 1:
# 
# 
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# Example 2:
# 
# 
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#
class Solution:
    # my solution
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input: return []
        if input.isdigit(): return [int(input)]
        res = []
        for i in range(len(input)):
            if not input[i].isdigit():
                sign = input[i]
                res_before = self.diffWaysToCompute(input[:i])
                res_after  = self.diffWaysToCompute(input[i+1:])
                for a in res_before:
                    for b in res_after:
                        res.append(self.eval(a, sign, b))
        return res

    def eval(self, a, sign, b):
        a, b = int(a), int(b)
        if sign == '+': return a + b
        if sign == '-': return a - b
        if sign == '*': return a * b
    
    # most-voted solution
    import re, operator
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        numbers = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
            if lo == hi:
                return [numbers[lo]]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]
        return build(0, len(numbers) - 1)

