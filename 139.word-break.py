#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (35.02%)
# Likes:    2204
# Dislikes: 122
# Total Accepted:    339.2K
# Total Submissions: 958.4K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#
class Solution:
    # TLE
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s.strip(): return True
        for w in wordDict:
            if w in s:
                wIndex = s.index(w)
                # remove s
                if self.wordBreak(s[:wIndex] + ' ' + s[wIndex + len(w):], wordDict):
                    return True
        return False
    
    # TLE
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return True
        for w in wordDict:
            # start at the beginning
            if w in s and not s.index(w):
                if self.wordBreak(s[len(w):], wordDict):
                    return True
        return False
    
    # My solution - Dynamic Programming
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # len(s) + 1
        # dp(i) -> s[: i] can be segmented into wordDict
        dp = [True] + [False for _ in range(len(s))]
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[i]: break 
                dp[i] = dp[j] and s[j: i] in wordDict
            # dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
        return dp[-1]
