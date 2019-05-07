#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in m:
                if len(stack) == 0:
                    return False
                if stack[-1] != m[c]:
                    return False
                _ = stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0


