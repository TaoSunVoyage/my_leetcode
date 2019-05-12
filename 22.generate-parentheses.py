#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    # my solution
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        if n == 1: return ['()']
        res = set()
        for s in self.generateParenthesis(n - 1):
            for i in range(len(s)):
                res.add(s[:i] + '()' + s[i:])
                if s[:i] == s[i:]:
                    break
        return list(res)
    
    # backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack()
        return res
