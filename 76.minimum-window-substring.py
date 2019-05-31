#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (30.51%)
# Likes:    2250
# Dislikes: 156
# Total Accepted:    236.6K
# Total Submissions: 768.3K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#
from collections import Counter
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     if not t: return ''
    #     if not s: return ''
    #     mapper = dict(zip(t, [len(s)]*len(t)))
    #     l = r = 0
    #     while l < len(s):
    #         if s[l] in mapper:
    #             mapper[s[l]] = l
    #             break
    #         l += 1
    #     else:
    #         return ''
        
    #     if max(mapper.values()) != len(s):
    #         minLength = len(mapper)
    #         res = s[l]
    #     else:
    #         minLength = len(s)
    #         res = ''
        
    #     r = l + 1
    #     while l <= r < len(s):
    #         if s[r] not in mapper:
    #             r += 1
    #         else:
    #             if mapper[s[r]] == l:
    #                 mapper[s[r]] = r
    #                 l = min(mapper.values())
    #             mapper[s[r]] = r
    #             r += 1
    #         if max(mapper.values()) != len(s):
    #             if r - l < minLength:
    #                 res = s[l: r+1]
    #                 minLength = r - l
    #     return res

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ''
        
        tCounter = Counter(t)
        required = len(tCounter)

        l = r = 0
        windowCounter = {}
        had = 0

        minLength = len(s) + 1
        res = ''
        
        while r < len(s):
            character = s[r]
            windowCounter[character] = windowCounter.get(character, 0) + 1

            if character in tCounter and tCounter[character] == windowCounter[character]:
                had += 1
            
            while l <= r and had == required:
                character = s[l]

                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    res = s[l: r + 1]
                
                windowCounter[character] -= 1
                if character in tCounter and tCounter[character] > windowCounter[character]:
                    had -= 1
                
                l += 1
            
            r += 1
        
        return res 


        
