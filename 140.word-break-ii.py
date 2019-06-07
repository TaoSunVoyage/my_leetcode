#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (27.11%)
# Likes:    927
# Dislikes: 241
# Total Accepted:    159.4K
# Total Submissions: 582.9K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
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
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
class Solution:
    # TLE
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        self.bfs(s, wordDict, [], res)
        return res
    def bfs(self, s, wordDict, path, res):
        if not s:
            if path:
                res.append(' '.join(path))
            return
        for w in wordDict:
            if s.startswith(w):
                self.bfs(s[len(w): ], wordDict, path + [w], res)
    
    # TLE
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [True] + [False] * len(s)
        mapper = {0: [[]]}
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    mapper[i] = mapper.get(i, []) +[ ws + [s[j: i]] for ws in mapper[j]]
        
        return [' '.join(ws) for ws in mapper.get(len(s), [])]


    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s] # memory !
        if not s: return []
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

