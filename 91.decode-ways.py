#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.18%)
# Likes:    1376
# Dislikes: 1581
# Total Accepted:    260.9K
# Total Submissions: 1.2M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution:
    # TLE -> it could be translated to dp!
    def numDecodings(self, s: str) -> int:
        if not s: 
            return 1
        res = 0
        if int(s[:1]) > 0:
            res += self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            res += self.numDecodings(s[2:])
        return res

    # Dynamic Programming
    def numDecodings(self, s: str) -> int:
        if not s: return 1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1: i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
    
    # Most-voted solution
    def numDecodings(self, s: str) -> int:
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w


                
            

    