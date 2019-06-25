#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (27.76%)
# Likes:    797
# Dislikes: 38
# Total Accepted:    113.5K
# Total Submissions: 402.7K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#
class Solution:
    # My solution - TLE
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if s1[0] == s2[0] == s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:]) | self.isInterleave(s1, s2[1:], s3[1:])
        if s1[0] == s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        return False
    
    # My solution - dynamic programming
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break
        for i in range(1, len(s2) + 1):
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = True
            else:
                break
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if dp[i][j - 1] and not dp[i - 1][j]:
                    dp[i][j] = s3[i + j - 1] == s2[j - 1]
                elif not dp[i][j - 1] and dp[i - 1][j]:
                    dp[i][j] = s3[i + j - 1] == s1[i - 1]
                elif dp[i][j - 1] and dp[i - 1][j]:
                    dp[i][j] = (s3[i + j - 1] == s2[j - 1]) | (s3[i + j - 1] == s1[i - 1])
                
                # or in one line
                # dp[i][j] = (dp[i][j - 1] & (s3[i + j - 1] == s2[j - 1])) | (dp[i - 1][j] & (s3[i + j - 1] == s1[i - 1]))
        
        return dp[-1][-1]


        

