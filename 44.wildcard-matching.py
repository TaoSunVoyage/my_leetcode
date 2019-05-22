#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (22.70%)
# Likes:    1009
# Dislikes: 69
# Total Accepted:    173.5K
# Total Submissions: 763.3K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# 
# 
#
class Solution:
    # My Solution
    # O(S*P) time, O(S*P) space
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic Programming
        # Row -> Pattern, Column -> String
        #     ' '  'a'  'a'
        # ' '  T    F    F
        # '*'  T    T    T
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        # ' ' matches ' '
        dp[0][0] = True
        # '*' matches empty string
        for i in range(1, len(p) + 1):
            dp[i][0] = dp[i - 1][0] and p[i - 1] == '*'
        # loop over the matrix dp
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[len(p)][len(s)]
    
    # Most-voted Solution: 
    # dynamic programming + back tracking
    # O(S*P) time, O(S) space
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) - p.count('*') > len(s):
            return False
        dp = [True] + [False] * len(s)
        for i in range(len(p)):
            if p[i] != '*':
                for j in reversed(range(len(s))):
                    dp[j + 1] = dp[j] and (p[i] == s[j] or p[i] == '?')
            else:
                for j in range(1, len(s) + 1):
                    dp[j] = dp[j-1] or dp[j]
            dp[0] = dp[0] and p[i] == '*'
        return dp[-1]

    # Time Complexity: best - O(min(S,P)), average - better than O(SlogP)
    # Space Complexity: O(1)
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1
 
        while s_idx < s_len:
            # If the pattern character = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern 
            elif star_idx == -1:
                return False
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        # The remaining characters in the pattern should all be '*' characters
        return all(x == '*' for x in p[p_idx:])

