#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    # # Time Limit Exceeded
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     for c in s:
    #         if c == '(':
    #             stack.append(c)
    #         else:
    #             if not stack or stack[-1] != '(':
    #                 return False
    #             else:
    #                 _ = stack.pop()
    #     return not stack

    # def longestValidParentheses(self, s: str) -> int:
    #     length = 0
    #     cache = []
    #     for i in range(len(s)):
    #         for j in range(i + 2, len(s) + 1):
    #             if (i, j) in cache:
    #                 continue
    #             if self.isValid(s[i:j]):
    #                 cache.append((i, j))
    #                 length = max(length, j - i)
    #                 for k in range(j + 2, len(s) + 1):
    #                     if self.isValid(s[j:k]):
    #                         cache.append((i, k))
    #                         length = max(length, k - i)
    #     return length
    
    # Dynamic Programming
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        max_to_now = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                # '()'
                if s[i-1] == '(':
                    dp[i] = 2 + dp[i-2]
                # '(())'
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = 2 + dp[i-1]
                    # '()(())'
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i - dp[i-1] - 2]
                max_to_now = max(max_to_now, dp[i])
        return max_to_now
    
    # Stack
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                _ = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans

    # No extra spaces
    # two-way loop
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxans = max(maxans, 2 * left)
            elif right > left:
                left = 0
                right = 0
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left == right:
                maxans = max(maxans, 2 * right)
            elif left > right:
                left = 0
                right = 0
        return maxans

        
